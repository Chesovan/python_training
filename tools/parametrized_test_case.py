import unittest

from configs.config import Config


class ParametrizedTestCase(unittest.TestCase):
    """
        TestCase classes that want to be parametrized should inherit
        from this class.
    """
    def __init__(self, method_name='runTest', browser=None, driver=None):
        super(ParametrizedTestCase, self).__init__(method_name)
        self.browser = browser
        self.driver = driver

    def setUp(self):
        """
            Initiates the driver with the desired browser defined as a parameter inside Config().
            :param browsersName: Refers to what browser you want to use
                                Supported browsers: Chrome, Firefox32, Firefox64, IE32, IE64.
                                Default value is 'None' and it uses Chrome.
                                In this case it inherits the parameter 'browser' from ParametrizedTestCase
                                so we can choose the browser upon calling the test in the test suite.
            :return: The webdriver instance
        """
        self.driver = Config(self.browser).get_driver()
        self.driver.maximize_window()

    @staticmethod
    def parametrize(testcase_class, browser=None):
        """
            Create a suite containing all tests taken from the given subclass,
            passing the parameter 'browser'.
        """

        test_loader = unittest.TestLoader()
        test_names = test_loader.getTestCaseNames(testcase_class)
        suite = unittest.TestSuite()
        for name in test_names:
            suite.addTest(testcase_class(name, browser=browser))
        return suite



    def tearDown(self):
        self.driver.quit()
