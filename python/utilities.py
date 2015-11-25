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

"""Checkers utilities.

Checkers protocol buffer helper functions.
"""

from google.protobuf import text_format

_CHECKERS_TEST_CASE = 'CHECKERS_TEST_CASE'
_CHECKERS_TEST_TEMPLATE = 'CHECKERS_TEST_TEMPLATE'


def LoadFromProtoFile(file_path, checkers_type, proto_type):
  proto_file = open(file_path)
  ascii_text = proto_file.read()
  proto_file.close()
  return ParseFromProtoText(ascii_text, checkers_type, proto_type)


def ParseFromProtoText(ascii_text, checkers_type, proto_type):
  proto = proto_type()
  text_format.Merge(ascii_text, proto)
  return checkers_type.FromProto(proto)
