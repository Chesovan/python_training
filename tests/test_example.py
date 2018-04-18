import unittest

from pages.academy_m30_page import AcademyMeine30Page
from pages.academy_m60_page import AcademyMeine60Page
from pages.academy_m90_page import AcademyMeine90Page
from pages.home_page import HomePage
from pages.page_example import PageExample
from pages.sc_registration import ScRegistationPage
from pages.academy_ospt_page import AcademyOsptPage
from tools.parametrized_test_case import ParametrizedTestCase

email = "joan.westling@pwp-academy.com"
password = "123qwe"
text_search = "Fascination"
text_search1 = "EARRINGS"

class TestExample(ParametrizedTestCase):

    @unittest.skip('pus in comment pana termin restul')
    def test_example1(self):
        '''
            self.driver is a parameter inherited from ParametrizedTestCase
        '''
        driver = self.driver
        driver.get('https://staging.pippajean.com/de/walter/')
        page_example = PageExample(driver)
        sc_registration = ScRegistationPage(driver)
        sc_registration.register_sc()

        #
        # page_example.click_sign_in_button()
        # page_example.enter_email(email)
        # page_example.enter_password(password)
        # page_example.click_login_button()

        # meine 30 did
        # pus in comment pana termion restul
        driver.get('https://staging-academy.pippajean.com/courses/meine-ersten-30-tage/')
        academy_m30_page = AcademyMeine30Page(driver)
        academy_m30_page.save_screen()
        academy_m30_page.complete_course()

        # # meine 60 did
        # # pus in comment pana termion restul
        driver.get('https://staging-academy.pippajean.com/courses/meine-ersten-60-tage/')
        academy_m60_page = AcademyMeine60Page(driver)
        academy_m60_page.save_screen()
        academy_m60_page.complete_course()

        # # # meine 90 did
        # # # pus in comment pana termion restul
        driver.get('https://staging-academy.pippajean.com/courses/meine-ersten-90-tage/')
        academy_m90_page = AcademyMeine90Page(driver)
        academy_m90_page.save_screen()
        academy_m90_page.complete_course()

        # ospm training todo finish it - dupa ultimul test (7) trebuie scos clickul pe bredcrumbs
        driver.get('https://staging-academy.pippajean.com/courses/online-style-party-training/')
        academy_ospt_page = AcademyOsptPage(driver)
        academy_ospt_page.complete_course()


    @unittest.skip('pus in comment pana termin restul')
    def test_example2(self):
        '''
            self.driver is a parameter inherited from ParametrizedTestCase
        '''
        driver = self.driver
        driver.get('https://staging.pippajean.com/de/walter/')
        page_example = PageExample(driver)
        sc_registration = ScRegistationPage(driver)
        # sc_registration.register_sc()

        #
        page_example.click_sign_in_button()
        page_example.enter_email(email)
        page_example.enter_password(password)
        page_example.click_login_button()

        # meine 30 did
        # pus in comment pana termion restul
        driver.get('https://staging-academy.pippajean.com/courses/meine-ersten-30-tage/')
        academy_m30_page = AcademyMeine30Page(driver)
        academy_m30_page.save_screen()
        academy_m30_page.complete_course()

        # # meine 60 did
        # # pus in comment pana termion restul
        driver.get('https://staging-academy.pippajean.com/courses/meine-ersten-60-tage/')
        academy_m60_page = AcademyMeine60Page(driver)
        academy_m60_page.save_screen()
        academy_m60_page.complete_course()

        # # # meine 90 did
        # # # pus in comment pana termion restul
        driver.get('https://staging-academy.pippajean.com/courses/meine-ersten-90-tage/')
        academy_m90_page = AcademyMeine90Page(driver)
        academy_m90_page.save_screen()
        academy_m90_page.complete_course()


    def test_scenarii_tema(self):
        '''
            self.driver is a parameter inherited from ParametrizedTestCase
        '''
        driver = self.driver
        driver.get('https://staging.pippajean.com/de/walter/')
        home_page = HomePage(driver)
        page_example = PageExample(driver)
        sc_registration = ScRegistationPage(driver)
        # sc_registration.register_sc()

        page_example.click_sign_in_button()
        page_example.enter_email(email)
        page_example.enter_password(password)
        page_example.click_login_button()

        # tema scenariul 1 todo
        home_page.input_search_field(text_search)
        home_page.click_search_button()
        home_page.get_search_result(text_search1)



