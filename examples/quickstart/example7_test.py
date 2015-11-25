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

"""Example Checkers test run that checks 1 + 1 = 2."""

from checkers.examples.quickstart import divide_tests
from checkers.examples.quickstart.calculator import Calculator
from checkers.python import checkers
from checkers.python.integrations.pyunit import pyunit


def CreateTestRun1():
  """Test run that will execute the defined test."""
  test_run = checkers.TestRun('calculator1')
  test_run.components.Register('calculator', Calculator())
  test_suite = checkers.TestSuite.FromProto(divide_tests.ParseTestSuiteProto())
  test_run.LoadTestSuite(test_suite)
  return test_run


def CreateTestRun2():
  """Test run that will execute the defined test."""
  test_run = checkers.TestRun('calculator2')
  test_run.components.Register('calculator', Calculator())
  test_suite = checkers.TestSuite.FromProto(divide_tests.ParseTestSuiteProto())
  test_run.LoadTestSuite(test_suite)
  return test_run


if __name__ == '__main__':
  pyunit.main([CreateTestRun1(), CreateTestRun2()])
