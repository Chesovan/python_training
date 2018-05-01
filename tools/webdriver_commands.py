from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

import unittest

from tools.parametrized_test_case import ParametrizedTestCase


class ElementNotFound(Exception):
    pass

class WebdriverCommands(ParametrizedTestCase):
    ELEMENT_WAIT = 30

    def __init__(self, driver):
        self.driver = driver
        self.driver.set_page_load_timeout(self.ELEMENT_WAIT)

    def wait_a_second(self, time=ELEMENT_WAIT):
        """
        Finds the webelement by the css selector or waits for it to be clickable and clicks it.
        :param css_selector: locator of the webelement.
        :param locator_description: description of the element we want to find
        :param time: how much time to wait for element to be clickable
        :return:
        """
        try:
            WebDriverWait(self.driver, time)
        except:
            raise ElementNotFound('Failed to wait a second')


    def click_element(self, css_selector, locator_description, time=ELEMENT_WAIT):
        """
        Finds the webelement by the css selector or waits for it to be clickable and clicks it.
        :param css_selector: locator of the webelement.
        :param locator_description: description of the element we want to find
        :param time: how much time to wait for element to be clickable
        :return:
        """
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))).click()
        except:
            raise ElementNotFound('Failed to locate: {}, using {}'.format(locator_description, css_selector))

    def send_keys(self, css_selector, locator_description, text, time=ELEMENT_WAIT):
        """
        Find the webelement by the css selector, waits for it to be visible and enters the wanted text in the field.
        :param css_selector: locator of the webelement
        :param locator_description: description of the element we want to find
        :param text: the text we want to enter in the field.
        :param time: how much time to wait for element to be present.
        :return:
        """
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))).send_keys(text)

        except:
            raise ElementNotFound('Failed to locate: {}, using {}'.format(locator_description, css_selector))

    def select_element_in_list(self,css_selector, selector_description, wanted_element, time=ELEMENT_WAIT):
        """
        Finds the list specified with the css selector and clicks on the wanted item.
        :param css_selector: locator of webelement list.
        :param selector_description: description of webelement
        :param wanted_element: element to be clickable after iteration through list.
        :param time: how much time to wait for element to be present.
        :return:
        """
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.CSS_SELECTOR , css_selector)))
            webelement_list = self.driver.find_elements_by_css_selector(css_selector)
            for item in webelement_list:
                if wanted_element in item.text:
                    item.click()
                    break
        except:
            raise ElementNotFound('Failed to locate: {}, using {}'.format(selector_description, css_selector))

    def get_web_element_attribute(self, css_selector, selector_description, attribute, time=ELEMENT_WAIT):
        """
        Finds webelement by css selector and returns the wanted attribute'
        :param css_selector: locator of webelement
        :param selector_description: description of webelement
        :param attribute: what attribute to return
        :param time: how much time to wait for element to be present.
        :return: the wanted attribute
        """
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
            return self.driver.find_element_by_css_selector(css_selector).get_attribute(attribute)
        except:
            raise ElementNotFound('Failed to locate: {}, using {}'.format(selector_description, css_selector))

    def get_web_element(self, css_locator, locator_description, time=ELEMENT_WAIT):
        """
        Finds a web element based on a provided css locator.
        :param css_locator: locator of the element we want to obtain
        :param locator_description: description of the element we want to obtain
        :return: <web element> The web element who's locator we specified as parameter
        """
        try:
            return WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_locator)))
        except:
            raise ElementNotFound("Failed to locate: {}, using: {}".format(locator_description, css_locator))

    def get_web_elements(self, css_locator, locator_description, time=ELEMENT_WAIT):
        """
        Finds web elements based on a provided css locator.
        :param css_locator: locator of the element we want to obtain
        :param locator_description: description of the element we want to obtain
        :return: <web element> The web elements found at the specified selector.
        """
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_locator)))
            return self.driver.find_elements_by_css_selector(css_locator)
        except:
            raise ElementNotFound("Failed to locate: {}, using: {}".format(locator_description, css_locator))

    def clear(self, css_selector, locator_description, time=ELEMENT_WAIT):
        """
            Clears field found at css selector
        :param css_selector: element selector
        :param locator_description: element description
        :param time: how much time to wait
        :return:
        """
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))).clear()
        except:
            raise ElementNotFound("Failed to locate: {}, using: {}".format(locator_description, css_selector))

    def get_text(self, css_selector, locator_description, time=ELEMENT_WAIT):
        '''
            Get text from element found at css selector
        :param css_selector: element selector
        :param locator_description: element description
        :param time: how much time to wait
        :return: text of found element
        '''
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
            return self.driver.find_element_by_css_selector(css_selector).text
        except:
            raise ElementNotFound("Failed to locate: {}, using: {}".format(locator_description, css_selector))

    def find_element_by_class_name(self, name):
        """
        Finds an element by class name.

        :Args:
         - name: The class name of the element to find.

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driver.find_element_by_class_name('foo')
        """
        try:
            return self.driver.find_element_by_class_name(name)
        except:
            raise ElementNotFound("Failed to locate: {}, using: {}".format('class ', name))

    def return_title(self):
        '''
            Returns page title
        :return: page title
        '''
        return self.driver.title

    def move_to_element(self, selector_id):
        element = self.driver.find_element_by_id(selector_id)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def move_to_element_css(self, selector):
        element = self.driver.find_element_by_css_selector(selector)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def select_from_dropdown(self, drop_id, x):
        select = Select(self.driver.find_element_by_css_selector(drop_id))
        # select by value
        select.select_by_value(x)

    # def change_element_class(self, el_class, element):
    #     self.driver.execute_script("arguments[0].setAttribute('class','bordered-box pitch clearfix starterkit-wrapper-active')", element)

    def save_screenshot(self, path):
        '''
            Takes screenshot of webdriver window.
        :param path: where do you want the file to be saved
        :return:
        '''
        self.driver.save_screenshot(path)

    def wait_for_element_to_disappear(self, selector, description, time= ELEMENT_WAIT):
        try:
            WebDriverWait(self.driver,time).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, selector)))
        except:
            raise ElementNotFound(selector,description)

    # def wait_for_element_to_appear(self, selector, description, time= ELEMENT_WAIT):
    #     try:
    #         WebDriverWait(self.driver,time).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, selector))) todo
    #     except:
    #         raise ElementNotFound(selector,description)