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

from checkers.python import checkers
from checkers.python.integrations.hamcrest import AssertThat
from checkers.python.integrations.hamcrest import EqualTo
from checkers.python.integrations.hamcrest import Is
from checkers.python.integrations.pyunit import pyunit

MODULE_NAME = __name__

TEST_CASE_PROTO = """
name: "TestZeroDividedBy%sEqualsZero"
description: "Tests that 0 / %d = 0."
data {
  name: "n"
  type: DECIMAL
  value: "%d"
}
implementation {
  python {
    template_name: "TestZeroDividedByNEquals0"
    module_name: "%s"
  }
}
"""


def BuildTestCase(number_text, number_value):
  proto_text = TEST_CASE_PROTO % (number_text, number_value,
                                  number_value, MODULE_NAME)
  test_case = checkers.TestCase.Parse(proto_text)
  return test_case


# @checkers.TestTemplate
# @checkers.TestData('n', checkers.Decimal, 'The number dividing 0.')
def TestZeroDividedByNEquals0(n):
  """Test template that verifies that 0 divided by any non-zero number is 0."""
  print '0 / %d = 0' % n
  quotient = 0 / n
  AssertThat(quotient, Is(EqualTo(0)))


TEST_DATA = {'One': 1, 'Two': 2, 'NegativeOne': -1, 'OneMillion': 1000000}


def CreateTestRun():
  """Test run that will execute the defined test."""
  test_run = checkers.TestRun()
  for number, value in TEST_DATA.iteritems():
    test_case = BuildTestCase(number, value)
    test_run.LoadTestCase(test_case)
    return test_run


if __name__ == '__main__':
  pyunit.main(CreateTestRun())
