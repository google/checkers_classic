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

"""Module containing all of the addition tests."""

from checkers.python import checkers
from checkers.python.validation import Assert


@checkers.Test
def TestOnePlusOneEqualsTwo(context):
  print '1 + 1 = 2'
  Assert.Equal(context, 1 + 1, 2)


@checkers.Test
def TestOnePlusTwoEqualsThree(context):
  print '1 + 2 = 3'
  Assert.Equal(context, 1 + 2, 3)
