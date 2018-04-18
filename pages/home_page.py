from tools.webdriver_commands import WebdriverCommands
import re

SEARCH_FIELD = {'css_selector': "#search", 'description': 'search field'}
SEARCH_FIELD_BUTTON = {'css_selector': "#search_mini_form > div > button", 'description': 'search button'}

class HomePage:

    def __init__(self, driver):
        self.page = WebdriverCommands(driver)

    # Search for a product
    def input_search_field(self, text):
        self.page.send_keys(SEARCH_FIELD['css_selector'], SEARCH_FIELD['description'], text)

    def click_search_button(self):
        self.page.click_element(SEARCH_FIELD_BUTTON['css_selector'], SEARCH_FIELD_BUTTON['description'])

    # Open product details
    price = 0
    def get_search_result(self, search_for):
        names = []
        # products = self.page.get_web_elements('.products.columncount-4  div.prod-box-name > a ', 'a')
        products = self.page.get_web_elements('.products.columncount-4 li', 'le')
        for product in products:
            print(product.text)
            names.append(product.text)
            if search_for in product.text:
                prices = re.findall("\d+\,\d+", product.text)
                price = prices[len(prices)-1]
                print(price)
                product.click()
                break

	# Check that price is the same as in results page
    def compare_prices(self, search_list_price):



	# Add product to cart
	# Check that product was added in the cart
	# Check the product price
	# Increase quantity
	# Check that product price is modified accordingly
