from tools.webdriver_commands import WebdriverCommands
SEARCH_FIELD = {'css_selector': "#search", 'description': 'search field'}
SEARCH_FIELD_BUTTON = {'css_selector': "#search_mini_form > div > button", 'description': 'search button'}
SIGN_IN_BUTTON = {'css_selector': "div.quick-wrap > div > ul > li > a", 'description': 'sign in button'}
EMAIL_FIELD = {'css_selector': "#email", 'description': 'email input field'}
PASSWORD_FIELD = {'css_selector': "#pass", 'description': 'email input field'}
LOGIN_BUTTON = {'css_selector': "#send2", 'description': 'login button'}
FIRST_SEARCH_RESULT = {'css_selector': ".container-fluid > div > ul > li:first-child > a", 'description': 'first search result'}
FIRST_SEARCH_RESULT_PRICE = {'css_selector': ".container-fluid > div > ul > li:first-child .price", 'description': ''}


# .container-fluid > div > ul > li:first-child  .price

# ACADEMY_TAB_BUTTON = {'css_selector':"a[title='Academy']", 'description': 'academy tab button'}


class PageExample:

    def __init__(self, driver):
        self.page = WebdriverCommands(driver)

    # def click_search_button(self):
    #     self.page.click_element(SEARCH_BUTTON['css_selector'], SEARCH_BUTTON['description'])

    def click_sign_in_button(self):
        self.page.click_element(SIGN_IN_BUTTON['css_selector'], SIGN_IN_BUTTON['description'])
        print('sign in was clicked')

    def enter_email(self, email):
        self.page.send_keys(EMAIL_FIELD['css_selector'], EMAIL_FIELD['description'], email)

    def enter_password(self, password):
        self.page.send_keys(PASSWORD_FIELD['css_selector'], PASSWORD_FIELD['description'], password)

    def click_login_button(self):
        self.page.click_element(LOGIN_BUTTON['css_selector'], LOGIN_BUTTON['description'])

    def verify_title(self):
        page_title = self.page.return_title()
        self.page.assertTrue('Title' == page_title, 'Expected: {}, received: {}'.format('Title', page_title))

    def enter_code(self, code_search):
        self.page.send_keys(SEARCH_FIELD['css_selector'], SEARCH_FIELD['description'], code_search)

    def click_search_button(self):
        self.page.click_element(SEARCH_FIELD_BUTTON['css_selector'], SEARCH_FIELD_BUTTON['description'])

    results_list_product_price = 0
    def get_search_result(self, x):
        items = self.page.get_web_elements('.container-fluid > div > ul','list')
        for item in items:
            text = item.text
            if x in text:
                self.results_list_product_price = item.find_element_by_css_selector('span.price').text
                item.click()
                break
        print(self.results_list_product_price)
