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

"""Checkers component_registry module.

Defines the checkers component registry module.
"""


class _ComponentRegistry(object):
  """Class responsible for managing components used in tests."""

  def __init__(self):
    self._components = {}

  def Lookup(self, component_id):
    return self._components[component_id]

  def Contains(self, component_id):
    return component_id in self._components

  def Register(self, component_id, component):
    self._components[component_id] = component

  def Unregister(self, component_id):
    del self._components[component_id]
