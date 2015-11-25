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

"""Checkers Logging module.

Defines logging functions of the checkers framework.
"""


class LogLevel(object):
  DEBUG = 40
  INFO = 30
  WARNING = 20
  ERROR = 10


class LogEntry(object):

  def __init__(self, level, message):
    self.level = level
    self.message = message


class Logger(object):
  """Logger for keeping track of log messages."""

  def __init__(self, level=LogLevel.INFO):
    self.level = level
    self.messages = []

  def __call__(self, level, message):
    if level <= self.level:
      print message
      self.messages.append(LogEntry(level, message))

  def Debug(self, message):
    self(LogLevel.DEBUG, message)

  def Info(self, message):
    self(LogLevel.INFO, message)

  def Warning(self, message):
    self(LogLevel.WARNING, message)

  def Error(self, message):
    self(LogLevel.ERROR, message)


