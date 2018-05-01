from pages.sc_registration import ScRegistationPage
from tools.webdriver_commands import WebdriverCommands
import re

SEARCH_FIELD = {'css_selector': "#search", 'description': 'search field'}
SEARCH_FIELD_BUTTON = {'css_selector': "#search_mini_form > div > button", 'description': 'search button'}
PRODUCT_DETAILS_PRICE = {'css_selector': "#product-price-4586 > span", 'description': 'product details price'}
ADD_TO_CART_BUTTON = {'css_selector': "#add-to-cart", 'description': 'add to cart button'}
TOP_CART_ICON = {'css_selector': "div.block-title > span", 'description': 'top cart icon'}
TO_SHOPPING_CART_BUTTON = {'css_selector': "a.button.btn.btn-primary", 'description': 'to shopping cart button'}
PRODUCT_SKU = {'css_selector': "div.product-main-info.clearfix > div > div.left > p", 'description': 'product sku'}
SHOPPING_CART_QTY_FIELD = {'css_selector': "#shopping-cart-50-table > tbody > tr:nth-child(1) > td:nth-child(3) > input", 'description': 'qty input field'}
CHECKOUT_BUTTON = {'css_selector': "div.cart > ul > li:nth-child(1) >button.button.gold-btn.host_bonus_alert", 'description': 'checkout'}
SUBMIT_STEP_1_BUTTON = {'css_selector': "#submit-step", 'description': 'submit step 1'}




class HomePage:

    def __init__(self, driver):
        self.page = WebdriverCommands(driver)
        self.sc_registration_page = ScRegistationPage(driver)

    # Search for a product
    def input_search_field(self, text):
        self.page.send_keys(SEARCH_FIELD['css_selector'], SEARCH_FIELD['description'], text)

    def click_search_button(self):
        self.page.click_element(SEARCH_FIELD_BUTTON['css_selector'], SEARCH_FIELD_BUTTON['description'])

    # Open product details
    list_price = 0
    product_sku = ''
    def get_search_result(self, search_for):
        names = []
        products = self.page.get_web_elements('.products.columncount-4 li', 'le')
        for product in products:
            # print(product.text)
            names.append(product.text)
            if search_for in product.text:
                prices = re.findall("\d+\,\d+", product.text)
                # product_sku =
                list_price = prices[len(prices) - 1]
                # print(list_price)
                product.click()
                break


    # Check that price is the same as in results page
    def compare_prices(self, list_price, comp_price):
        if ("{0:.2f}".format(comp_price)) == ("{0:.2f}".format(list_price)):
            return True
        else:
            return False

    def shopping_cart_price_list(self):
        price = []
        products = self.page.get_web_elements('#mini-cart  .item-price > table > tbody > tr > td > span', 'li')
        for product in products:
            print(product.text)
            float_nr = re.findall("\d+\,\d+", product.text)
            price.append(float_nr[0])
        if self.compare_prices(self.list_price, price[0]):
            print('Price in the cart is the same as price in the initial search results list')
        else:
            print('Price in the cart is different than the price in the initial search results list')

    def increment_first_item_qty(self):
        self.page.clear(SHOPPING_CART_QTY_FIELD['css_selector'], SHOPPING_CART_QTY_FIELD['description'])
        self.page.send_keys(SHOPPING_CART_QTY_FIELD['css_selector'], SHOPPING_CART_QTY_FIELD['description'], 2)
        self.page.send_keys(SHOPPING_CART_QTY_FIELD['css_selector'], SHOPPING_CART_QTY_FIELD['description'], '\n')
        # temporar todo trebie facut dinamic


    def shopping_cart_items_list(self, sku_search):
        # > td > h2
        tr_texts = self.page.get_web_elements('#shopping-cart-50-table > tbody > tr', 'li')
        for sku in tr_texts:
            text_to_string = sku.text
            sku_from_codes = text_to_string.split('\n')
            if sku_search == sku_from_codes[2]:
                prices_4_splited = sku_from_codes[4].split('€')
                discounted_price = float(prices_4_splited[2].replace(',', '.'))
                full_price = float(prices_4_splited[0].replace(',', '.'))
                if self.compare_prices(discounted_price, (full_price/2)):
                    self.increment_first_item_qty()
                    print('Price is the same and has a 50% discount')
                else:
                    print('Price is not the same')

            tr_texts = self.page.get_web_elements('#shopping-cart-25-table > tbody > tr', 'li')
            for sku in tr_texts:
                text_to_string = sku.text
                sku_from_codes = text_to_string.split('\n')
                print(sku_from_codes[2])
                if sku_search == sku_from_codes[2]:
                    print(sku_from_codes[1])
                    prices_4_splited = sku_from_codes[4].split('€')
                    discounted_price = float(prices_4_splited[2].replace(',', '.'))
                    full_price = float(prices_4_splited[0].replace(',', '.'))

                    if self.compare_prices(discounted_price, (full_price / 4)*3):
                        print('Price is the same and has a 25% discount')
                    else:
                        print('Price is not the same')
                break
            break

    def scenario_1(self, text, search_for, holder):
        self.input_search_field(text)
        self.click_search_button()
        self.get_search_result(search_for)
        product_code = self.page.get_web_element(PRODUCT_SKU['css_selector'], PRODUCT_SKU['description'])
        product_sku = product_code.text[-6:]
        self.page.click_element(ADD_TO_CART_BUTTON['css_selector'], ADD_TO_CART_BUTTON['description'])
        try:
            self.page.click_element('a.button.btn.btn-prima','wait', 4)
        except:
            pass
        self.page.click_element(TOP_CART_ICON['css_selector'], TOP_CART_ICON['description'])
        self.page.move_to_element('mini-cart')
        try:
            self.page.click_element('a.button.btn.btn-prima','wait', 2)
        except:
            pass
        self.page.click_element(TO_SHOPPING_CART_BUTTON['css_selector'], TO_SHOPPING_CART_BUTTON['description'], 5)

        self.shopping_cart_items_list(product_sku)

        self.page.click_element(CHECKOUT_BUTTON['css_selector'], CHECKOUT_BUTTON['description'])
        self.page.wait_a_second(5)
        # todo: de aici in jos sa stricat ceva, repara!
        try:
            self.page.move_to_element('submit-step')
            self.page.click_element(SUBMIT_STEP_1_BUTTON['css_selector'], SUBMIT_STEP_1_BUTTON['description'], 5)
        except:
            self.page.move_to_element('submit-step')
            self.page.click_element(SUBMIT_STEP_1_BUTTON['css_selector'], SUBMIT_STEP_1_BUTTON['description'])
        self.sc_registration_page.select_payment_option(holder)
        self.page.wait_a_second(5)
        self.sc_registration_page.click_submit_confirmation_button()








    # Check the product price
    # Increase quantity
    # Check that product price is modified accordingly
