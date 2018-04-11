from tools.webdriver_commands import WebdriverCommands
from pages.page_example import PageExample
import names


SC_REGISTER_LINK = {'css_selector': "div.columns.last > ul > li:nth-child(7) > a", 'description': 'register as style coach link'}
SC_FIRSTNAME_FIELD = {'css_selector': "#firstname", 'description': 'sc reg first name'}
SC_LASTNAME_FIELD = {'css_selector': "#lastname", 'description': 'sc reg last name'}
SC_DOB_SELECTOR_FIELD = {'css_selector': "div.input-box > #dateofbirth-dp", 'description': 'date of birth selector'}
SC_DOB_DAY_SELECTOR = {'css_selector': " td.ui-datepicker-days-cell-over.ui-datepicker-current-day > a", 'description': 'pick a date'}
SC_EMAIL_FIELD = {'css_selector': "#email_address", 'description': 'enter email'}
SC_PASSWORD_FIELD = {'css_selector': "#password", 'description': 'password field'}
SC_CONFIRM_PASSWORD_FIELD = {'css_selector': "#confirmation", 'description': 'confirm password field'}
SC_STREET_FIELD = {'css_selector': "#street_1", 'description': 'street_1'}
SC_HOUSE_NR_FIELD = {'css_selector': "#house_number", 'description': 'house number'}
SC_ZIP_FIELD = {'css_selector': "#zip", 'description': 'zip'}
SC_CITY_FIELD = {'css_selector': "#city", 'description': 'city'}
SC_TELEPHONE_FIELD = {'css_selector': "#telephone", 'description': 'telephone'}
SC_ACCEPT_CHECKBOX = {'css_selector': "#accept-checkbox", 'description': 'accept checkbox'}
SC_SUBMIT_STEP_BUTTON = {'css_selector': "#submit-step", 'description': 'submit step'}
SC_REF_FIELD = {'css_selector': "#stylistref", 'description': 'stylist ref'}
SC_STARTER_SET_SMALL_RADIO = {'css_selector': "div.starter-kit.pj-stylist > div:nth-child(5) > div.left.img-wrap", 'description': 'starter set small'}
SC_REG_BANK_PAYMENT_OPTION= {'css_selector': "#paymentMethods > li:nth-child(4) > input", 'description': 'payment methods'}
SC_REG_CARD_PAYMENT_OPTION= {'css_selector': "#paymentMethods > li:nth-child(1) > input", 'description': 'payment methods'}
CARD_NUMBER_FIELD = {'css_selector': "input[id='card.cardNumber']", 'description': 'card number'}
CARD_HOLDER_FIELD = {'css_selector': "input[id='card.cardHolderName']", 'description': 'holder name'}
CVC_FIELD = {'css_selector': "input[id='card.cvcCode']", 'description': 'cvc'}
CARD_EXPIRY_DATE = {'month_css_selector': "select[id='card.expiryMonth']", 'year_css_selector': "select[id='card.expiryYear']"}
SC_PAY_BUTTON= {'css_selector': "input[class='paySubmit paySubmitcard']", 'description': 'pay button'}
SC_TERMS_CHECKBOX = {'css_selector': "#terms", 'description': 'terms'}
SC_SUBMIT_CONFIRMATION_BUTTON = {'css_selector': "#submit-confirmation-step", 'description': 'submit confirmation'}
SC_BACK_TO_HOMEPAGE_BUTTON = {'css_selector': "div.buttons-set.to-the-left > a > span", 'description': 'submit confirmation'}

class ScRegistationPage:

    def __init__(self, driver):
        self.page = WebdriverCommands(driver)
        self.pageExaple = PageExample(driver)


    def click_register_sc_link(self):
        self.page.click_element(SC_REGISTER_LINK['css_selector'], SC_REGISTER_LINK['description'])

    def enter_sc_firstname(self, firstname):
        self.page.send_keys(SC_FIRSTNAME_FIELD['css_selector'], SC_FIRSTNAME_FIELD['description'], firstname)

    def enter_sc_lastname(self, lastname):
        self.page.send_keys(SC_LASTNAME_FIELD['css_selector'], SC_LASTNAME_FIELD['description'], lastname)

    def select_date_of_birth(self):
        self.page.click_element(SC_DOB_SELECTOR_FIELD['css_selector'], SC_DOB_SELECTOR_FIELD['description'])
        self.page.send_keys(SC_DOB_SELECTOR_FIELD['css_selector'], SC_DOB_SELECTOR_FIELD['description'], '\n')

    def enter_sc_email(self, email):
        self.page.send_keys(SC_EMAIL_FIELD['css_selector'], SC_EMAIL_FIELD['description'], email)

    def enter_and_confirm_password(self, password):
        self.page.send_keys(SC_PASSWORD_FIELD['css_selector'], SC_PASSWORD_FIELD['description'], password)
        self.page.send_keys(SC_CONFIRM_PASSWORD_FIELD['css_selector'], SC_CONFIRM_PASSWORD_FIELD['description'], password)

    def enter_sc_address_reg(self, street, nr, plz, city, phone):
        self.page.send_keys(SC_STREET_FIELD['css_selector'], SC_STREET_FIELD['description'], street)
        self.page.send_keys(SC_HOUSE_NR_FIELD['css_selector'], SC_HOUSE_NR_FIELD['description'], nr)
        self.page.send_keys(SC_ZIP_FIELD['css_selector'], SC_ZIP_FIELD['description'], plz)
        self.page.send_keys(SC_CITY_FIELD['css_selector'], SC_CITY_FIELD['description'], city)
        self.page.select_from_dropdown('#country', 'DE')
        self.page.send_keys(SC_TELEPHONE_FIELD['css_selector'], SC_TELEPHONE_FIELD['description'], phone)

    def click_accept_checkbox(self):
        self.page.click_element(SC_ACCEPT_CHECKBOX['css_selector'], SC_ACCEPT_CHECKBOX['description'])

    def click_submit_button(self):
        self.page.click_element(SC_SUBMIT_STEP_BUTTON['css_selector'], SC_SUBMIT_STEP_BUTTON['description'])

    def enter_sc_ref(self, ref):
        self.page.send_keys(SC_REF_FIELD['css_selector'], SC_REF_FIELD['description'], ref)

    def click_on_small_starter_set(self):
        self.page.move_to_element_css('div.starter-kit.pj-stylist > div:nth-child(5) > div.left.img-wrap')
        # self.page.click_element(SC_STARTER_SET_SMALL_RADIO['css_selector'], SC_STARTER_SET_SMALL_RADIO['description'])
        # self.page.change_element_class('bordered-box pitch clearfix starterkit-wrapper-active', 'div.register-ajax > div.starter-kit.pj-stylist > div:nth-child(5)')

    def select_payment_option(self, holder):
        # self.page.click_element(SC_REG_BANK_PAYMENT_OPTION['css_selector'], SC_REG_BANK_PAYMENT_OPTION['description'])
        # self.page.wait_a_second(10)
        # # self.page.click_element(SC_PAY_BUTTON['css_selector'], SC_PAY_BUTTON['description'])
        # self.page.move_to_element_css('#pmmdetails-bankTransfer_DE > table > tbody > tr:nth-child(2) > td > div > input')

        self.page.click_element(SC_REG_CARD_PAYMENT_OPTION['css_selector'], SC_REG_CARD_PAYMENT_OPTION['description'])
        try:
            self.page.click_element('#card.cardNumb', 'Waiting..', 5)
        except:
            pass
        self.page.move_to_element('card.cardNumber')
        self.page.send_keys(CARD_NUMBER_FIELD['css_selector'], CARD_NUMBER_FIELD['description'], '4111111111111111')
        self.page.send_keys(CARD_HOLDER_FIELD['css_selector'], CARD_HOLDER_FIELD['description'], holder)
        self.page.select_from_dropdown(CARD_EXPIRY_DATE['month_css_selector'], '08')
        self.page.select_from_dropdown(CARD_EXPIRY_DATE['year_css_selector'], '2018')
        self.page.send_keys(CVC_FIELD['css_selector'], CVC_FIELD['description'], '737')
        self.page.click_element(SC_PAY_BUTTON['css_selector'], SC_PAY_BUTTON['description'])



    def click_submit_confirmation_button(self):
        self.page.click_element(SC_TERMS_CHECKBOX['css_selector'], SC_TERMS_CHECKBOX['description'])
        self.page.click_element(SC_SUBMIT_CONFIRMATION_BUTTON['css_selector'], SC_SUBMIT_CONFIRMATION_BUTTON['description'])

    def click_back_to_homepage(self):
        self.page.click_element(SC_BACK_TO_HOMEPAGE_BUTTON['css_selector'], SC_BACK_TO_HOMEPAGE_BUTTON['description'])


    def register_sc(self):
        self.click_register_sc_link()

        firstname = names.get_first_name(gender='female')
        self.enter_sc_firstname(firstname)

        lastname = names.get_last_name()
        self.enter_sc_lastname(lastname)

        self.select_date_of_birth()

        email = firstname + '.' + lastname + '@pwp-academy.com'
        self.enter_sc_email(email.lower())

        password = '123qwe'
        self.enter_and_confirm_password(password)

        self.enter_sc_address_reg('Breitenau', '54', '91555', 'Feuchtwangen', '025486695477')

        self.click_accept_checkbox()

        self.click_submit_button()

        self.enter_sc_ref('wpsc')

        self.click_submit_button()

        # self.click_on_small_starter_set()

        self.click_submit_button()

        holder = firstname + ' ' + lastname
        self.select_payment_option(holder)

        self.page.wait_a_second(5)

        self.click_submit_confirmation_button()

        self.click_back_to_homepage()

        self.pageExaple.user_login(email, password)
