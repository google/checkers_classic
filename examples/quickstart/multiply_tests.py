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

"""Example test that shows how to create a set of tests using one method.

This is an example that doesn't use the data-driven proto-defined apprpoach.
"""

from checkers.python import checkers
from checkers.python.integrations.hamcrest import AssertThat
from checkers.python.integrations.hamcrest import EqualTo
from checkers.python.integrations.hamcrest import Is


# This is the test function that has a bunch of parameters that may or may not
# be overridden.
def TestMultiply(x=1, y=1, product=1):
  print x, y, product
  AssertThat(x * y, Is(EqualTo(product)))

# The first element in the tuple is the description, the second element is the
# test parameters. How this data is set up is totally flexible; you just want to
# have enough information to pass into the FunctionTestCase method.
TEST_DATA = {
    '1x1': ('Multiplies 1x1, checks it is 1', {}),
    '1x2': ('Multiplies 1x2, checks it is 2', {'y': 2, 'product': 2}),
    '2x2': ('Multiplies 2x2, checks it is 4', {'x': 2, 'y': 2, 'product': 4}),
}


# Creates the set of test cases from the test function and the test data.
def CreateTestCasesForMultiply():
  """Test run that will execute the defined test."""
  test_cases = []
  for name, data in TEST_DATA.iteritems():
    test_case = checkers.FunctionTestCase(TestMultiply, test_data=data[1],
                                          name='TestMultiplyWith%s' % name,
                                          description=data[0])
    test_cases.append(test_case)
  return test_cases


# Export tests makes the test cases that are passed in look like they were
# decorated by checkers.Test.
checkers.ExportTests(CreateTestCasesForMultiply())
