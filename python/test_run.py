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

"""Checkers TestRun.

Defines a TestRun in the checkers framework.
"""

import inspect
import os

from component_registry import _ComponentRegistry
from test_case import TestCase
from test_suite import TestSuite


class TestRun(object):
  """Test run is a collection of test cases/suites."""
  _DEFAULT_SUITE_NAME = ''

  def __init__(self, name=None):
    stack_frame = inspect.stack()[1]
    filename = stack_frame[1]
    parts = filename.split(os.sep)
    google3_index = len(parts) - 1 - parts[::-1].index('google3')
    relative_path = os.sep.join(parts[google3_index:])
    self.module = os.path.splitext(relative_path)[0]

    self.name = name if name else os.path.basename(self.module)
    self.components = _ComponentRegistry()
    self.suites = {}
    self.test_cases = {}
    self.setup = []
    self.teardown = []
    self.test_case_setup = []
    self.test_case_teardown = []

  def RegisterSetUpFunction(self, setup):
    self.setup.append(setup)

  def RegisterTearDownFunction(self, teardown):
    self.teardown.append(teardown)

  def RegisterTestCaseSetUpFunction(self, setup):
    self.test_case_setup.append(setup)

  def RegisterTestCaseTearDownFunction(self, teardown):
    self.test_case_teardown.append(teardown)

  def RegisterComponent(self, component_id, component):
    self.components.Register(component_id, component)

  def UnregisterComponent(self, component_id):
    self.components.Unregister(component_id)

  def LoadTestsFromModule(self, module, suite_name=None):
    suite_name = suite_name if suite_name else ''   # module.__name__
    suite_description = module.__doc__
    test_suite = TestSuite(suite_name, suite_description)
    for attr_name in dir(module):
      attr = getattr(module, attr_name)
      if isinstance(attr, TestCase):
        test_suite.AddTestCase(attr)
    self.LoadTestSuite(test_suite)

  def LoadTestSuite(self, test_suite):
    for test_case in test_suite.test_cases.values():
      self.LoadTestCase(test_case, test_suite.name)

  def LoadTestCase(self, test_case, suite_name=None):
    # suite_name = suite_name if suite_name else TestRun._DEFAULT_SUITE_NAME
    suite_name = '%s.%s' % (self.name, suite_name) if suite_name else self.name
    self.test_cases[test_case.name] = test_case
    self.CreateTestSuite(suite_name)
    self.suites[suite_name].AddTestCase(test_case)

  def CreateTestSuite(self, suite_name=None, suite_description=''):
    suite_name = suite_name if suite_name else TestRun._DEFAULT_SUITE_NAME
    if suite_name not in self.suites:
      self.suites[suite_name] = TestSuite(suite_name, suite_description)
