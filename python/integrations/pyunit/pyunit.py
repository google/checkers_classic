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

"""Module that integrates PyUnit (unittest) with Checkers.

This module provides an integration with PyUnit. Note that this requires at
least Python 2.7 to work because that's when load_tests was added to PyUnit.

This allows us to run Checkers tests through the PyUnit framework. Simply build
up the PyUnitTestRun just as you would a normal Checkers TestRun in the
load_tests method of the main module and return the pyunit_suite.

Note that this will just add the Checkers tests to whatever tests that PyUnit
would have run anyway.

Example:

from wherever import foo_tests  # Contains the checkers.TestCase functions.

def load_tests(loader, tests, pattern):
  test_run = PyUnitTestRun(loader, tests)
  test_run.LoadTestCasesFromModule(foo_tests, 'FooTests')
  return test_run.pyunit_suite

if __name__ == '__main__':
  unittest.main()
"""

import gflags
import sys
import traceback
import unittest
from checkers.python import checkers


FLAGS = gflags.FLAGS


def _ListOfTestsGenerator(s):
  tests = []
  for test in s:
    if unittest.suite._isnotsuite(test):
      tests.append(type(test))
    else:
      tests += _ListOfTestsGenerator(test)
  return tests


class PyUnitTestSuite(unittest.TestCase):

  def setUp(self):
    for setup in self.test_run.test_case_setup:
      setup(self.test_run)

  def tearDown(self):
    for teardown in self.test_run.test_case_teardown:
      teardown(self.test_run)

  @classmethod
  def setUpClass(cls):
    # print "SetUp for test run %s" % cls.test_run.name
    for setup in cls.test_run.setup:
      setup(cls.test_run)

  @classmethod
  def tearDownClass(cls):
    # print "TearDown for test run %s" % cls.test_run.name
    for teardown in cls.test_run.teardown:
      teardown(cls.test_run)


class PyUnitTestRun(object):
  """PyUnit wrapper for a checkers TestRun.

  This class can be used the same way as a checkers.TestRun class. The
  difference is that it has been extended to support converting a Checkers test
  run into a PyUnit test suite.
  """

  def __init__(self, test_runs, pyunit_tests=None,
               test_case_type=unittest.TestCase):
    self.test_runs = test_runs
    self.pyunit_tests = pyunit_tests
    self.test_case_type = test_case_type

  @property
  def pyunit_test_cases(self):
    return _ListOfTestsGenerator(self.pyunit_suite)

  @property
  def pyunit_suite(self):
    """Gets the unittest.TestSuite containing all of the tests.

    This will return all of the tests that will be run including both Checkers
    tests and normal PyUnit tests.

    Returns:
      unittest.TestSuite: The suite containing the PyUnit-ified test cases.
    """
    pyunit_suite = unittest.TestSuite()

    # Add the tests discovered by PyUnit.
    if self.pyunit_tests:
      pyunit_suite.addTest(self.pyunit_tests)

    # Add the tests defined by Checkers.
    loader = unittest.defaultTestLoader
    loader.testMethodPrefix = 'Test'
    for test_run in self.test_runs:
      for suite in test_run.suites.values():
        pyunit_test_case = self._CreatePyUnitTestCaseSuite(suite, test_run)
        pyunit_suite.addTest(loader.loadTestsFromTestCase(pyunit_test_case))
    return pyunit_suite

  def _CreatePyUnitTestCaseSuite(self, suite, test_run):
    """Creates a TestCase object that represents the Checkers test suite.

    Sorry for the naming here, but PyUnit is really confusing in that a TestCase
    is actually a class representing a test suite. So this method is converting
    a Checkers TestSuite into a PyUnit TestCase with a bunch of Test* methods.

    Args:
      suite: checkers.TestSuite, The test suite PyUnit needs to execute.
      test_run: checkers.TestRun, The test run that is executing.

    Returns:
      unittest.TestCase: The TestCase class containing the suite's test cases.
    """
    test_methods = {}
    for test_case_name, test_case in suite.test_cases.iteritems():
      test_closure = test_case.CreateTestClosure(test_run.components,
                                                 test_suite=suite,
                                                 test_run=test_run)
      test_methods[test_case_name] = self._CreatePyUnitTestMethod(test_closure)
      test_case_name = 't' + test_case_name[1:]
      test_methods[test_case_name] = self._CreatePyUnitTestMethod(test_closure)
    test_methods['test_run'] = test_run
    cls = type(suite.name, (PyUnitTestSuite,), test_methods)
    cls.__module__ = test_run.module
    return cls

  def _CreatePyUnitTestMethod(self, test_closure):
    """Creates a method that can be called by the PyUnit framework.

    By default, each test method gets passed the TestCase instance when it gets
    called by PyUnit, so this wrapper just takes that test case and throws it
    away.

    Args:
      test_closure: function, The test case with all of the args assigned.

    Returns:
      function: The test method that ignores the test_case parameter.
    """

    def PyUnitTestMethod(test_case):  # pylint: disable=unused-argument
      """Wrapper function that discards the test_case and calls the test method.

      Args:
        test_case: unittest.TestCase, The executing test case (ignored).
      """
      test_closure()

    test_method = PyUnitTestMethod
    test_method.func_name = test_closure.func_name
    if not test_method.func_name.startswith('Test'):
      test_method.func_name = 'Test' + test_method.func_name
    test_method.func_doc = test_closure.func_doc
    return test_method


def LoadTests(test_runs, include_pyunit_tests, module=None):
  """Function that takes in the tests that PyUnit has already discovered."""
  if not module:
    module = sys.modules['__main__']

  def LoadWrapper(loader, tests, pattern):  # pylint: disable=unused-argument,g-line-too-long
    if not include_pyunit_tests:
      tests = unittest.TestSuite()
    result = None
    try:
      result = PyUnitTestRun(test_runs, tests).pyunit_suite
    except:
      traceback.print_exc()
      raise
    return result

  setattr(module, 'load_tests', LoadWrapper)

_SHUTDOWN_HOOKS = {}


def RegisterShutdownHook(test_name, shutdown_hook_function):
  if test_name not in _SHUTDOWN_HOOKS:
    _SHUTDOWN_HOOKS[test_name] = []
  _SHUTDOWN_HOOKS[test_name].append(shutdown_hook_function)


def _ShutdownHook(result):
  checkers.Shutdown()
  for hooks in _SHUTDOWN_HOOKS.values():
    for hook in hooks:
      hook(result)


def main(test_run, *args, **kwargs):
  test_runs = test_run
  if not isinstance(test_runs, list):
    test_runs = [test_run]
  if 'module' in kwargs:
    LoadTests(test_runs, kwargs.pop('include_pyunit_tests', True),
              module=kwargs['module'])
  else:
    LoadTests(test_runs, kwargs.pop('include_pyunit_tests', True))
  if 'unittest_shutdown_hook' in kwargs:
    RegisterShutdownHook('global', kwargs['unittest_shutdown_hook'])
  kwargs['unittest_shutdown_hook'] = _ShutdownHook
  return unittest.main(argv=[sys.argv[0]])

