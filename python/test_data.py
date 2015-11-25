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

"""Checkers TestData.

Defines representation of TestData in the checkers framework.
"""

from decimal import Decimal
import utilities
from google.protobuf import text_format
# pylint: disable=g-direct-third-party-import
from checkers import checkers_pb2


class TestData(object):
  """Represents the data that can be made available to a test."""

  def __init__(self, name, data_type, value_text, proto_type=None):
    self.name = name
    self.type = data_type
    self.value_text = value_text
    self.proto_type = proto_type

  @property
  def value(self):
    if self.type == checkers_pb2.TestData.STRING:
      return self.value_text
    if self.type == checkers_pb2.TestData.DECIMAL:
      return Decimal(self.value_text)
    if self.type == checkers_pb2.TestData.PROTO:
      proto = self.proto_type()
      text_format.Merge(self.value_text, proto)
      return proto

  @staticmethod
  def Parse(proto_text):
    return utilities.ParseFromProtoText(proto_text, TestData,
                                        checkers_pb2.TestData)

  @staticmethod
  def Load(proto_path):
    return utilities.LoadFromProtoFile(proto_path, TestData,
                                       checkers_pb2.TestData)

  @staticmethod
  def FromProto(proto):
    test_data = TestData(str(proto.name), proto.type, proto.value)
    return test_data

