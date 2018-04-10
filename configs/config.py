from selenium import webdriver


class Configuration(object):

    def __init__(self, browser_name=None):
        """
            Takes the browser name, verifies it and creates an instance of it.
            :param browser_name: refers to what browser you want to use.
            If no browser is defined or the defined one is not supported, it opens by default Chrome.
        """
        if browser_name == 'Chrome':
            path = '../drivers/chromedriver.exe'
            self.driver = webdriver.Chrome(path)

        elif browser_name == 'Firefox32':
            path = '../drivers/geckodriver32.exe'
            self.driver = webdriver.Firefox(executable_path=path)

        elif browser_name == 'Firefox64':
            path = '../drivers/geckodriver64.exe'
            self.driver = webdriver.Firefox(executable_path=path)

        elif browser_name == 'IE32':
            path = '../drivers/IEDriverServer32.exe'
            self.driver = webdriver.Ie(executable_path=path)

        elif browser_name == 'IE64':
            path = '../drivers/IEDriverServer64.exe'
            self.driver = webdriver.Ie(executable_path=path)
        else:
            path = '../drivers/chromedriver.exe'
            self.driver = webdriver.Chrome(path)



class Config(Configuration):

    def get_driver(self):
        return self.driver
