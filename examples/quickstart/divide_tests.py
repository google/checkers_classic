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

"""Defines division tests for the checkers framework examples.

Example tests for the checkers framework.
"""

from checkers import checkers_pb2
from checkers.python.validation import Assert
from google.protobuf import text_format

MODULE_NAME = __name__

################################################################################
# Test Template
################################################################################


# @checkers.TestTemplate
# @checkers.TestData('n', checkers.Decimal, 'The number dividing 0.')
def TestZeroDividedByNEquals0(context, calculator, n):
  """Test template that verifies that 0 divided by any non-zero number is 0."""
  print '0 / %d = 0' % n
  quotient = calculator.Divide(0, n)
  Assert.Equal(context, quotient, 0)

################################################################################
# Test Data (ASCII format)
################################################################################


SAMPLE_TEST_SUITE_PROTO_ASCII = """
name: "ZeroDividendTests"
test_case {
  name: "TestZeroDividedByOneEqualsZero"
  description: "Tests that 0 / 1 = 0."
  data {
    name: "n"
    type: DECIMAL
    value: "1"
  }
  implementation {
    python {
      template_name: "TestZeroDividedByNEquals0"
      module_name: "%s"
    }
  }
}
test_case {
  name: "TestZeroDividedByNegativeOneEqualsZero"
  description: "Tests that 0 / -1 = 0."
  data {
    name: "n"
    type: DECIMAL
    value: "-1"
  }
  implementation {
    python {
      template_name: "TestZeroDividedByNEquals0"
      module_name: "%s"
    }
  }
}
test_case {
  name: "TestZeroDividedByNegativeOneMillionEqualsZero"
  description: "Tests that 0 / 1000000 = 0."
  data {
    name: "n"
    type: DECIMAL
    value: "1000000"
  }
  implementation {
    manual: "Divide 0 by n."
    python {
      template_name: "TestZeroDividedByNEquals0"
      module_name: "%s"
    }
  }
}
""" % (MODULE_NAME, MODULE_NAME, MODULE_NAME)


def ParseTestSuiteProto(ascii=SAMPLE_TEST_SUITE_PROTO_ASCII):
  print SAMPLE_TEST_SUITE_PROTO_ASCII
  test_suite_proto = checkers_pb2.TestSuite()
  text_format.Merge(ascii, test_suite_proto)
  return test_suite_proto


################################################################################
# Test Data (Programmatic)
################################################################################


def _BuildTestCaseProtos():
  """Helper function that populates a list of TestCase protos."""
  n_dict = {'One': 1, 'NegativeOne': -1, 'OneMillion': 1000000}
  test_case_protos = []
  for n_name, n_value in n_dict.iteritems():
    test_case_proto = checkers_pb2.TestCase()
    test_case_proto.name = 'TestZeroDividedBy%sEquals0' % n_name
    test_case_proto.description = 'Tests that 0 / %d = 0.' % n_value
    data = test_case_proto.data.add()
    data.name = 'n'
    data.value = str(n_value)
    data.type = checkers_pb2.TestData.DECIMAL
    python = test_case_proto.implementation.python.add()
    python.template_name = 'TestZeroDividedByNEquals0'
    python.module_name = MODULE_NAME
    test_case_protos.append(test_case_proto)
  return test_case_protos


def BuildTestSuiteProto():
  """This is a programmatic way to create the same proto as the text represents.

  See documentation on the proto2 api in order to understand what this code is
  doing. The end result is that it will create a protocol buffer that looks
  exactly like the one written out in ASCII format above.

  Returns:
    checkers_pb2.TestSuite
  """
  test_suite = checkers_pb2.TestSuite()
  test_suite.name = 'ZeroDividendTests'
  test_suite.test_case.extend(_BuildTestCaseProtos())
  return test_suite
