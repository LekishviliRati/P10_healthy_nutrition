import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# **********
from better_nutrition.settings import BASE_DIR

# firefox_options = webdriver.FirefoxOptions()
# firefox_options.headless = True
# **********


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    # **********
    # def setUp(self):
    #     geckodriver = str(BASE_DIR / "webdrivers" / "geckodriver")
    #     self.browser = webdriver.Firefox(
    #         executable_path=geckodriver, options=firefox_options
    #     )
    # **********

    def tearDown(self):
        self.browser.quit()

    def test_registration(self):
        # Check if Django is working
        self.browser.get('http://localhost:8000')
        self.browser.set_window_size(1024, 768)
        # self.browser.maximize_window()
        self.assertIn('Pur Beurre', self.browser.title)
        time.sleep(3)

        # Check if Visitor succeed to reach login page.
        # registration_page = self.browser.find_element_by_id('Inscription')
        wait = WebDriverWait(self.browser, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, 'Inscription')))
        element.click()

        # registration_page.click()
        time.sleep(3)

        # Fill connexion fields and enter
        first_name_box = self.browser.find_element_by_id('id_first_name')
        first_name_box.send_keys('Jean')
        time.sleep(2)
        last_name_box = self.browser.find_element_by_id('id_last_name')
        last_name_box.send_keys('Martin')
        time.sleep(2)
        email_box = self.browser.find_element_by_id('id_email')
        email_box.send_keys('jean.martin2@gmail.com')
        time.sleep(2)
        password1_box = self.browser.find_element_by_id('id_password1')
        password1_box.send_keys('Django_74')
        time.sleep(2)
        password2_box = self.browser.find_element_by_id('id_password2')
        password2_box.send_keys('Django_74')
        time.sleep(2)
        password2_box.send_keys(Keys.ENTER)
        time.sleep(7)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
