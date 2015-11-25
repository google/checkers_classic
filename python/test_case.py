# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

"""Defines a checkers TestCase.

Defines the TestCase class and other related helper functions.
"""

import imp
import inspect
import os
from os import path
import sys

import context as ctx
from test_data import TestData
import test_result
import utilities
# pylint: disable=g-direct-third-party-import
from checkers import checkers_pb2


# pylint: disable=missing-docstring


def _LookupModule(module_name, module_path=None):
  base_path = os.getcwd()
  if module_name not in sys.modules:
    if module_path is None:
      path_parts = module_name.split('.')
      module_path = ''
      for part in path_parts:
        module_path = path.join(module_path, part)
      module_path += '.py'
    if not path.isabs(module_path):
      module_path = path.join(base_path, module_path)
    print 'Loading %s from %s' % (module_name, module_path)
    imp.load_source(module_name, module_path)
  module = sys.modules[module_name]
  return module


def LookupFunction(module_name, template_name, module_path=None):
  module = _LookupModule(module_name, module_path)
  parts = template_name.split('.')
  function = module
  for part in parts:
    function = getattr(function, part)
  return function


def FindImplementation(test_case_proto):
  for impl in test_case_proto.implementation.python:
    try:
      module_path = None
      if impl.HasField('module_path'):
        module_path = impl.module_path
      function = LookupFunction(impl.module_name, impl.template_name,
                                module_path)
      return function
    except:  # pylint: disable=bare-except
      pass
  return None


class TestCase(object):

  def __init__(self, name, description):
    self.name = str(name)
    self.description = str(description)
    self.component_map = {}

  def MapComponent(self, parameter_name, component_id):
    self.component_map[parameter_name] = component_id

  def __call__(self, context, **components):
    raise NotImplementedError(
        'The subclassed TestCase must implement the __call__ method.')

  # pylint: disable=unused-argument
  def CreateTestClosure(self, components, test_suite=None, test_run=None,
                        context_factory=ctx.Context):
    args = {}
    for parameter_name, component_id in self.component_map.iteritems():
      if components.Contains(component_id):
        args[parameter_name] = components.Lookup(component_id)
    context = context_factory(self, args=dict(args), test_run=test_run)

    def TestCaseClosure():
      self.__call__(context, **args)
    closure = TestCaseClosure
    closure.__name__ = self.name
    closure.__doc__ = self.description
    return closure

  @staticmethod
  def Parse(proto_text):
    return utilities.ParseFromProtoText(proto_text, TestCase,
                                        checkers_pb2.TestCase)

  @staticmethod
  def Load(proto_path):
    return utilities.LoadFromProtoFile(proto_path, TestCase,
                                       checkers_pb2.TestCase)

  @staticmethod
  def FromProto(proto):
    template_function = FindImplementation(proto)
    test_data = {}
    for data_proto in proto.data:
      data = TestData.FromProto(data_proto)
      test_data[data.name] = data.value
    test_case = _FunctionWrappingTestCase(template_function, test_data,
                                          proto.name, proto.description)
    return test_case


class _FunctionWrappingTestCase(TestCase):

  def __init__(self, test_case_function, test_data=None,
               name=None, description=None):
    """Creates a test case out of a function.

    Args:
      test_case_function: The function that the test case will call.
      test_data: dict containing kwargs to pass into the function.
      name: name of the test case.
      description: description of the test case.
    """
    name = name if name else test_case_function.func_name
    description = description if description else test_case_function.func_doc
    super(_FunctionWrappingTestCase, self).__init__(name, description)
    self.function = test_case_function
    self.data = test_data if test_data else {}
    args = inspect.getargspec(test_case_function).args
    for parameter_name in args:
      if parameter_name in self.data or parameter_name == args[0]:
        continue
      self.MapComponent(parameter_name, None)

  def __call__(self, context, *args, **components):
    context.test_result = test_result.TestResult.RUNNING
    kwargs = {}
    # Include default values
    argspec = inspect.getargspec(self.function)
    arglen = len(argspec.args) if argspec.args else 0
    deflen = len(argspec.defaults) if argspec.defaults else 0
    for i in xrange(deflen):
      kwargs[argspec.args[arglen - 1 - i]] = argspec.defaults[deflen - 1 - i]
    kwargs.update(components)
    kwargs.update(self.data)
    total = arglen - deflen
    if args:
      diff = 0
      if argspec.args[0] == 'context' or argspec.args[0] == '_':
        diff = -1
      for i in range(total):
        kwargs[argspec.args[i]] = args[i + diff]
    # If the function expects an arg (e.g. a late-bound component)
    for arg in argspec.args:
      if arg == 'context' or arg == '_':
        kwargs[arg] = context
      if context.test_run.components.Contains(arg):
        kwargs[arg] = context.test_run.components.Lookup(arg)
    output = self.function(**kwargs)
    if not output:
      output = type(context.test_case.name, (object,), {})
      output = output()
    setattr(output, 'context', context)
    if context.test_result == test_result.TestResult.RUNNING:
      context.test_result = test_result.TestResult.PASSED
    return output

