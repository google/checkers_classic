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

"""Checkers TestSuite.

Defines a TestSuite in the checkers framework.
"""

from test_case import TestCase
import utilities
# pylint: disable=g-direct-third-party-import
from checkers import checkers_pb2


class TestSuite(object):
  """Represents a collection of tests."""

  def __init__(self, name, description='', test_cases=None):
    self.name = name
    self.description = description
    self.test_cases = {}
    test_cases = test_cases if test_cases else []
    for test_case in test_cases:
      self.AddTestCase(test_case)

  def AddTestCase(self, test_case):
    self.test_cases[test_case.name] = test_case

  def RemoveTestCase(self, test_case_name):
    del self.test_cases[test_case_name]

  @staticmethod
  def Parse(proto_text):
    return utilities.ParseFromProtoText(proto_text, TestSuite,
                                        checkers_pb2.TestSuite)

  @staticmethod
  def Load(proto_path):
    return utilities.LoadFromProtoFile(proto_path, TestSuite,
                                       checkers_pb2.TestSuite)

  @staticmethod
  def FromProto(proto):
    test_suite = TestSuite(str(proto.name), str(proto.description))
    for test_case_proto in proto.test_case:
      test_case = TestCase.FromProto(test_case_proto)
      test_suite.AddTestCase(test_case)
    return test_suite

