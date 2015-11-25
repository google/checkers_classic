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

"""Assertions used by the checkers framework.

Defines assertions used in test cases.
"""

import logging
from test_result import TestResult


class Assert(object):
  """Class that provides the ability to assert some behavior."""
  _CAUSE_FAILURE = True
  _IS_FATAL = True
  _LOG_LEVEL = logging.LogLevel.ERROR

  def __init__(self, test):
    self.test = test

  @classmethod
  def _Assert(cls, context, condition, message):
    if not condition:
      if cls._CAUSE_FAILURE:
        context.log(cls._LOG_LEVEL, 'Assertion failed: %s' % message)
        context.test_result = TestResult.FAILED
      if cls._IS_FATAL:
        raise AssertionError(message)
    context.log.Debug('Assertion passed')

  @classmethod
  def True(cls, context, condition, message):
    cls._Assert(context, condition, message)

  @classmethod
  def False(cls, context, condition, message):
    cls._Assert(context, not condition, message)

  @classmethod
  def Equal(cls, context, x, y, message=None):
    message = message if message else '[%s] != [%s]' % (x, y)
    cls._Assert(context, x == y, message)

  @classmethod
  def NotEqual(cls, context, x, y, message=None):
    message = message if message else '[%s] == [%s]' % (x, y)
    cls._Assert(context, x != y, message)

  @classmethod
  def Raises(cls, context, exception_type, method, *args):
    """Asserts that the provided exception is raised."""
    def _PrintError(exception_type, message=None):
      if message:
        return '%s: %s' % (exception_type.__name__, message)
      return exception_type.__name__

    try:
      method(*args)
    except exception_type:
      return
    except Exception as ex:
      raise AssertionError('Expected %s, got %s' %
                           (_PrintError(exception_type),
                            _PrintError(type(ex), ex.message)))
    cls._Assert(context, False, 'Expected exception %s'
                % _PrintError(exception_type))


class Verify(Assert):
  _CAUSE_FAILURE = True
  _IS_FATAL = False
  _LOG_LEVEL = logging.LogLevel.ERROR


class Check(Assert):
  _CAUSE_FAILURE = False
  _IS_FATAL = False
  _LOG_LEVEL = logging.LogLevel.WARNING
