from tools.webdriver_commands import WebdriverCommands


class HomePage:

    def __init__(self, driver):
        self.page = WebdriverCommands(driver)

    def input_search_field(self, text):
        self.page.send_keys('css', 'desc', text)