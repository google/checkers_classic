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

"""Module that wraps PyHamcrest with Checkers.

The main reason this module exists is because PyHamcrest has some cool support
for matchers, but they don't align with Google's coding guidelines. So if users
use PyHamcrest directly (which they are more than welcome to do), then create
custom matchers, they'll either need to follow PyHamcrest's style which will
result in lint messages everywhere, or they'd need to follow Google's style
which would result in weird-looking test code that's part Googley, part not.
"""

from __future__ import absolute_import

# pylint: disable=g-bad-import-order

# Basic Matchers
from hamcrest.core import assert_that
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.core import equal_to
from hamcrest.core.core import is_
from hamcrest.core.core.isinstanceof import instance_of
from hamcrest.core.helpers.hasmethod import hasmethod
from hamcrest.library.object.haslength import has_length
from hamcrest.library.object.hasstring import has_string

# Number based Matchers
from hamcrest.library.number.ordering_comparison import greater_than
from hamcrest.library.number.ordering_comparison import greater_than_or_equal_to
from hamcrest.library.number.ordering_comparison import less_than
from hamcrest.library.number.ordering_comparison import less_than_or_equal_to

# Text Matchers
from hamcrest.library.text.isequal_ignoring_case import equal_to_ignoring_case
from hamcrest.library.text.isequal_ignoring_whitespace import equal_to_ignoring_whitespace
from hamcrest.library.text.stringcontains import contains_string
from hamcrest.library.text.stringendswith import ends_with
from hamcrest.library.text.stringstartswith import starts_with

# Logical Matchers
from hamcrest.core.core.allof import all_of
from hamcrest.core.core.anyof import any_of
from hamcrest.core.core.isanything import anything
from hamcrest.core.core.isnot import is_not

# Sequence Matchers
from hamcrest.library.collection.isin import is_in
from hamcrest.library.collection.issequence_containing import has_item
from hamcrest.library.collection.issequence_containing import has_items
from hamcrest.library.collection.issequence_containinginanyorder import contains_inanyorder
from hamcrest.library.collection.issequence_containinginorder import contains
from hamcrest.library.collection.issequence_onlycontaining import only_contains

# Dictionary Matchers
from hamcrest.library.collection.isdict_containing import has_entry
from hamcrest.library.collection.isdict_containingkey import has_key
from hamcrest.library.collection.isdict_containingvalue import has_value

# Decorator Matchers (syntatic sugar)
from hamcrest.core.core.is_ import is_

# pylint: enable=g-bad-import-order

# pylint: disable=g-bad-name

hasmethod = hasmethod
BaseMatcher = BaseMatcher

AssertThat = assert_that
EqualTo = equal_to
Is = is_
InstanceOf = instance_of
HasLength = has_length
HasString = has_string

GreaterThan = greater_than
GreaterThanOrEqualTo = greater_than_or_equal_to
LessThan = less_than
LessThanOrEqualTo = less_than_or_equal_to

EqualToIgnoringCase = equal_to_ignoring_case
EqualToIgnoringWhitespace = equal_to_ignoring_whitespace
ContainsString = contains_string
EndsWith = ends_with
StartsWith = starts_with

AllOf = all_of
AnyOf = any_of
Anything = anything
IsNot = is_not

IsIn = is_in
HasItem = has_item
HasItems = has_items
ContainsInAnyOrder = contains_inanyorder
Contains = contains
OnlyContains = only_contains

HasEntry = has_entry
HasKey = has_key
HasValue = has_value

# pylint: enable=g-bad-name
