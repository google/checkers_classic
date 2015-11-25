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

"""Example Checkers test run that checks a few arithmetic functions."""

from checkers.python import checkers
from checkers.python.integrations.hamcrest import AssertThat
from checkers.python.integrations.hamcrest import EqualTo
from checkers.python.integrations.hamcrest import Is
from checkers.python.integrations.pyunit import pyunit


@checkers.Test
def TestOnePlusOneEqualsTwo():
  print '1 + 1 = 2'
  AssertThat(1 + 1, Is(EqualTo(2)))


@checkers.Test
def TestOnePlusTwoEqualsThree():
  print '1 + 2 = 3'
  AssertThat(1 + 2, Is(EqualTo(3)))


@checkers.Test
def TestOneMinusOneEqualsZero():
  print '1 - 1 = 0'
  AssertThat(1 - 1, Is(EqualTo(0)))


@checkers.Test
def TestThreeMinusTwoEqualsOne():
  print '3 - 2 = 1'
  AssertThat(3 - 2, Is(EqualTo(1)))


def CreateAdditionTestsSuite():
  test_suite = checkers.TestSuite('AdditionTests')
  test_suite.AddTestCase(TestOnePlusOneEqualsTwo)
  test_suite.AddTestCase(TestOnePlusTwoEqualsThree)
  return test_suite


def CreateSubtractionTestsSuite():
  test_suite = checkers.TestSuite('SubtractionTests')
  test_suite.AddTestCase(TestOneMinusOneEqualsZero)
  test_suite.AddTestCase(TestThreeMinusTwoEqualsOne)
  return test_suite


def CreateTestRun():
  """Test run that will execute the defined test."""
  test_run = checkers.TestRun()
  test_run.LoadTestSuite(CreateAdditionTestsSuite())
  test_run.LoadTestSuite(CreateSubtractionTestsSuite())
  return test_run


if __name__ == '__main__':
  pyunit.main(CreateTestRun())
