import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Authentication(unittest.TestCase):
    USERNAME = 'admin'
    PASSWORD = 'admin'

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)

    def tearDown(self):
        self.chrome.quit()

    # @unittest.skip
    def test_auth(self):
        self.chrome.get('https://' + self.USERNAME + ':' + self.PASSWORD + '@the-internet.herokuapp.com/basic_auth')
        sleep(3)

# https://admin:admin@the-internet.herokuapp.com/basic_auth -> Pagina formatata fara variabile