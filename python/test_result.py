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

"""Checkers TestResult.

Defines a TestResult in the checkers framework.
"""


class TestResult(object):
  """Constants representing a test result."""
  INVALID = 0
  READY = 1
  RUNNING = 2
  PASSED = 3
  FAILED = 4
  SKIPPED = 5
  _strings = {0: 'INVALID', 1: 'READY', 2: 'RUNNING',
              3: 'PASSED', 4: 'FAILED', 5: 'SKIPPED'}

  @classmethod
  def String(cls, value):
    if value not in cls._strings:
      return cls.String(cls.INVALID)
    return cls._strings[value]
