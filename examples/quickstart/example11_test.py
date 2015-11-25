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

"""Example Checkers tests with setup and teardown hooks."""

from checkers.python import checkers
from checkers.python.integrations.hamcrest import AssertThat
from checkers.python.integrations.hamcrest import EqualTo
from checkers.python.integrations.hamcrest import Is
from checkers.python.integrations.pyunit import pyunit


@checkers.Test
def TestOnePlusOneEqualsTwo(name):
  print '1 + 1 = 2'
  print 'printing name: %s' % name
  AssertThat(1 + 1, Is(EqualTo(2)))


@checkers.Test
def TestZeroPlusOneEqualsOne(context):
  print '1 + 1 = 2'
  print 'printing name: %s' % context.test_run.components.Lookup('name')
  AssertThat(1 + 1, Is(EqualTo(2)))


@checkers.Test
def TestTwoPlusTwoEqualsFour(_, calculator):
  AssertThat(2 + 2, Is(EqualTo(calculator.Add(2, 2))))


def CreateTestRun():
  """Test run that will execute the defined test."""
  test_run = checkers.TestRun()
  # For per-test setup/teardown (once per test case).
  test_run.RegisterTestCaseSetUpFunction(TestCaseSetUp)
  test_run.RegisterTestCaseTearDownFunction(TestCaseTearDown)
  # For per-test run setup/teardown (once per test run).
  test_run.RegisterSetUpFunction(TestRunSetUp)
  test_run.RegisterTearDownFunction(TestRunTearDown)
  # Actual test cases.
  test_run.LoadTestCase(TestOnePlusOneEqualsTwo)
  test_run.LoadTestCase(TestZeroPlusOneEqualsOne)
  return test_run


def TestCaseSetUp(test_run):
  print 'running test case setup for test_run %s' % test_run.name
  test_run.RegisterComponent('name', 'phooey')


def TestCaseTearDown(test_run):
  print 'running test case teardown for test_run %s' % test_run.name
  test_run.UnregisterComponent('name')


def TestRunSetUp(test_run):
  print 'running setup method for test_run %s' % test_run.name


def TestRunTearDown(test_run):
  print 'running teardown method for test_run %s' % test_run.name


if __name__ == '__main__':
  pyunit.main(CreateTestRun())
