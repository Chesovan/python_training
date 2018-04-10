import unittest

from pages.page_example import PageExample
from pages.academy_ospt_page import AcademyOsptPage
from tools.parametrized_test_case import ParametrizedTestCase

email = "sc.wp3@evozon.com"
password = "123qwe"
text_search = "Fascination"
text_search1 = "Earrings"

class TestExample(ParametrizedTestCase):

    def test_example1(self):
        '''
            self.driver is a parameter inherited from ParametrizedTestCase
        '''
        driver = self.driver
        driver.get('https://staging.pippajean.com/de/')
        page_example = PageExample(driver)
        # page_example.click_search_button()
        page_example.click_sign_in_button()
        page_example.enter_email(email)
        page_example.enter_password(password)
        page_example.click_login_button()

        # tema scenariul 1
        # page_example.enter_code(text_search)
        # page_example.click_search_button()
        # page_example.get_search_result(text_search1)

        driver.get('https://staging-academy.pippajean.com/courses/online-style-party-training/')
        academy_ospt_page = AcademyOsptPage(driver)
        academy_ospt_page.click_mache_dieses_training_button()
        academy_ospt_page.click_lesson1()
        academy_ospt_page.click_mark_complete_button()
        academy_ospt_page.click_mark_complete_button()
        academy_ospt_page.click_quiz_on_lesson3()
        academy_ospt_page.click_start_quiz_button()
        academy_ospt_page.lesson_quiz(3)

        # home_page = HomePage(driver)
        # home_page.input_search_field('Search text')

    @unittest.skip('Reason')
    def test_example2(self):
        '''
            self.driver is a parameter inherited from ParametrizedTestCase
        '''
        driver = self.driver
        driver.get('https://www.myprotein.ro')
        page_example = PageExample(driver)
        page_example.click()

    @unittest.skip('Reason2')
    def test_example3(self):
        '''
            self.driver is a parameter inherited from ParametrizedTestCase
        '''
        driver = self.driver
        driver.get('https://www.myprotein.ro')
        x = PageExample(driver)
        x.click()
        x.verify_title()



