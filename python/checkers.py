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

"""Checkers module.

Defines the primary top-level checkers constructs and setup and shutdown
hooks.
"""

import functools
import inspect

import context as ctx
from test_case import _FunctionWrappingTestCase
from test_case import TestCase
from test_run import TestRun
from test_suite import TestSuite

################################################################################
# Stubs (for convenience when using Checkers)
################################################################################

# pylint: disable=unused-argument
# pylint: disable=g-bad-name

TestCase = TestCase
TestSuite = TestSuite
TestRun = TestRun
FunctionTestCase = _FunctionWrappingTestCase
# pylint: enable=g-bad-name

################################################################################
# Decorators
################################################################################


def Test(function):
  test_case = _FunctionWrappingTestCase(function)
  return test_case


def TestData(name, data_type, description):
  def Decorator(function):
    @functools.wraps(function)
    def CallableFunction(*args, **kwargs):
      function(*args, **kwargs)
    return CallableFunction
  return Decorator


def Component(name, description):
  def Decorator(function):
    @functools.wraps(function)
    def CallableFunction(*args, **kwargs):
      function(*args, **kwargs)
    return CallableFunction
  return Decorator


def TestTemplate(function):
  @functools.wraps(function)
  def CallableFunction(*args, **kwargs):
    function(*args, **kwargs)
  return CallableFunction


################################################################################
# Export Test Cases
#
# On the occasions when a module wants to make a set of test cases available to
# Checkers without having to add each test case in the list to the module by
# hand, use the checkers.ExportTestCases method. Just give it a list of
# functions that have been 'decorated' by checkers.Test.
################################################################################
def ExportTests(test_cases):
  stack_frame = inspect.stack()[1]
  module = inspect.getmodule(stack_frame[0])
  for test_case in test_cases:
    setattr(module, test_case.name, test_case)

_SHUTDOWN_HOOKS = {}


def RegisterShutdownHook(test, waiter_function):
  """Methods that are called before the test run is completed.

  An example of where this comes in handy is when there is an asynchronous call
  and you want to wait for the callback to be called before exiting the test.
  This gives a mechanism to block the full test run from ending without
  blocking other tests from running.

  Args:
    test: The test that is being run where the hook needs to run.
    waiter_function: The function that waits to be called.
  """
  key = test.test_case.name
  if key not in _SHUTDOWN_HOOKS:
    _SHUTDOWN_HOOKS[key] = []
  _SHUTDOWN_HOOKS[key].append(waiter_function)


def Shutdown():
  for hooks in _SHUTDOWN_HOOKS.values():
    for hook in hooks:
      hook()


def Output(name, fields):
  t = type(name, (object,), fields)
  return t()


def DefaultContext(testcase, testrun=None):
  if not testrun:
    testrun = TestRun('default')
  return ctx.Context(testcase, test_run=testrun)


def RunTest(fwtc, *args, **kwargs):
  context = DefaultContext(fwtc)
  fwtc(context, *args, **kwargs)
