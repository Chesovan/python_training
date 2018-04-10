import unittest

from tests.test_login import TestLogin
from tools.parametrized_test_case import ParametrizedTestCase
from pyunitreport import HTMLTestRunner
from tests.test_example import TestExample


def create_test_suite():
    suite = unittest.TestSuite()
    # suite.addTest(ParametrizedTestCase.parametrize(TestExample, 'Firefox64'))
    # suite.addTest(ParametrizedTestCase.parametrize(TestExample, 'IE64'))
    suite.addTest(ParametrizedTestCase.parametrize(TestExample, 'Chrome'))
    # suite.addTest(ParametrizedTestCase.parametrize(TestLogin))

    return suite


suite = create_test_suite()

runner = HTMLTestRunner(output='../../Reporting', report_name='Report file')
runner.run(suite)
