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

"""Checkers context.

Defines the Context class, a basic building block of checkers tests.
"""

import gflags
import logging
import test_result


FLAGS = gflags.FLAGS


class _DataRegistry(object):

  def __init__(self):
    self.data = {}

  def SetValue(self, key, value):
    self.__dict__[key] = value
    self.data[key] = value


class Context(object):

  def __init__(self, test_case, test_run=None, logger=None,
               args=None, data=None):
    self.test_case = test_case
    self.test_run = test_run
    # pylint: disable=no-value-for-parameter
    self.log = logger if logger else logging.Logger()
    self.args = args
    self.test_result = test_result.TestResult.READY
    self.data = _DataRegistry()
    for key, flag in FLAGS.FlagDict().iteritems():
      self.data.SetValue(key, flag.value)
    data = data if data else {}
    for key, value in data.iteritems():
      self.data.SetValue(key, value)
