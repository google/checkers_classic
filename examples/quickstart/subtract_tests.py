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

"""Module containing all of the subtraction tests."""

from checkers.python import checkers
from checkers.python.validation import Assert


@checkers.Test
def TestOneMinusOneEqualsZero(context):
  print '1 - 1 = 0'
  Assert.Equal(context, 1 - 1, 0)


@checkers.Test
def TestThreeMinusTwoEqualsOne(context):
  print '3 - 2 = 1'
  Assert.Equal(context, 3 - 2, 1)
