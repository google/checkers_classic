### Checkers Python Unit Test Framework
This is not an official Google product.

Checkers is released under the Apache 2.0 license.  See the LICENSE file for details.

Checkers is a python unit test framework for defining data-driven tests.

Contributions are not being accepted for this code as there are significant updates with non-backwards-compatible changes in the release pipeline which will bring new features to the framework.  Even fundamentals such as the way tests are defined will change.  Because of this, if you wish to use this package it is strongly recommended that you fork this repository.

Checkers builds on top of the standard python unittest module.  It also includes the assertions from the python Hamcrest library.

The best documentation is the tests themselves, which are located in examples/quickstart/example#_test.py.  Example 9 was depricated, however the file remains so that test results are consistent in historical tracking.

Checkers is used most-simply as follows:

 * Create a TestRun object
 * Load one or more test cases (functions with a @checkers.Test decorator and assertion statements in them)
 * Pass the test run as the argument the pyunit wrapper/integration as pyunit.main(TestRun_object)
 
Test suites in checkers can have overlapping test cases (two suites can contain the same test).  The runner ensures that the test is only executed once if both suites are run.  A TestRun can contain multiple TestSuites.  See example2_test.py

Tests can be automatically discovered to some degree by module, see example3_test.py

There is some support for creating test suites from a protocol buffer, but this support will be dropped in the next version.  If this is relied upon it is *strongly* recommended to fork this repository.

Checkers also allows the specification of startup/setup and shutdown callbacks.  See example8_test.py and example11_test.py.

