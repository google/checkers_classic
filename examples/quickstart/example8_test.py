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

"""Example Checkers test run that checks 1 + 1 = 2 with a shutdown hook."""

from checkers.examples.quickstart.calculator import Calculator
from checkers.python import checkers
from checkers.python.integrations.hamcrest import AssertThat
from checkers.python.integrations.hamcrest import EqualTo
from checkers.python.integrations.hamcrest import Is
from checkers.python.integrations.pyunit import pyunit
from checkers.python.test_result import TestResult


def ContextProcessorShutdownHook(context):
  def _ShutdownHook():
    print 'it\'s checkers, foo!!', TestResult.String(context.test_result)
  return _ShutdownHook


@checkers.Test
def TestOnePlusOneEqualsTwo(context):
  print '1 + 1 = 2'
  AssertThat(1 + 1, Is(EqualTo(2)))
  checkers.RegisterShutdownHook(context, ContextProcessorShutdownHook(context))


@checkers.Test
def TestTwoPlusTwoEqualsFour(_, calculator):
  AssertThat(2 + 2, Is(EqualTo(calculator.Add(2, 2))))


def CreateTestRun():
  """Test run that will execute the defined test."""
  test_run = checkers.TestRun()
  test_run.RegisterComponent('calculator', Calculator())
  test_run.LoadTestCase(TestOnePlusOneEqualsTwo)
  test_run.RegisterSetUpFunction(SetUp1)
  test_run.RegisterSetUpFunction(SetUp2)
  test_run.RegisterTearDownFunction(TearDown1)
  test_run.RegisterTearDownFunction(TearDown2)
  return test_run


def SetUp1(test_run):
  print 'running first setup method for test_run %s' % test_run.name


def SetUp2(test_run):
  print 'running second setup method for test_run %s' % test_run.name


def TearDown1(test_run):
  print 'running first teardown method for test_run %s' % test_run.name


def TearDown2(test_run):
  print 'running second teardown method for test_run %s' % test_run.name


if __name__ == '__main__':
  # To run a test method directly
  ctx = checkers.DefaultContext(TestOnePlusOneEqualsTwo)
  TestOnePlusOneEqualsTwo(ctx)
  checkers.RunTest(TestOnePlusOneEqualsTwo)
  # Extra arguments just get ignored by checkers, but the more
  # correct behavior would probably be to have this raise an error.
  checkers.RunTest(TestOnePlusOneEqualsTwo, Calculator())

  # ctx = checkers.DefaultContext(TestTwoPlusTwoEqualsFour)
  # TestTwoPlusTwoEqualsFour(Calculator())
  checkers.RunTest(TestTwoPlusTwoEqualsFour, Calculator())

  pyunit.main(CreateTestRun())
