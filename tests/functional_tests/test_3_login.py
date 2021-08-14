import unittest
import time
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# **********
from better_nutrition.settings import BASE_DIR

# firefox_options = webdriver.FirefoxOptions()
# firefox_options.headless = True
# **********

opts = FirefoxOptions()
opts.add_argument("--headless")


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(firefox_options=opts)

    # def setUp(self):
    #     self.browser = webdriver.Firefox()

    # **********
    # def setUp(self):
    #     geckodriver = str(BASE_DIR / "webdrivers" / "geckodriver")
    #     self.browser = webdriver.Firefox(
    #         executable_path=geckodriver, options=firefox_options
    #     )
    # **********

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        # Check if Django is working
        self.browser.get('http://localhost:8000')
        # self.browser.set_window_size(1024, 768)
        self.browser.maximize_window()
        self.assertIn('Pur Beurre', self.browser.title)
        time.sleep(3)

        # Check if Visitor succeed to reach login page.
        login_page = self.browser.find_element_by_id('Connexion')
        login_page.click()
        time.sleep(3)

        # Fill connexion fields and enter
        email_box = self.browser.find_element_by_id('id_username')
        email_box.send_keys('jean.martin2@gmail.com')
        time.sleep(2)
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys('Django_74')
        time.sleep(2)
        password_box.send_keys(Keys.ENTER)
        time.sleep(7)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
