from tools.parametrized_test_case import ParametrizedTestCase


class TestLogin(ParametrizedTestCase):


    def test_successfull_login(self):
        driver = self.driver
        driver.get('URL')
