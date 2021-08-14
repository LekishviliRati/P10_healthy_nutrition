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


class NewVisitorTest(unittest.TestCase):

    # def setUp(self):
    #     self.browser = webdriver.Firefox()

    # # **********
    def setUp(self):
        geckodriver = str(BASE_DIR / "usr" / "local" / "bin" / "geckodriver")
        self.browser = webdriver.Firefox(
            executable_path=geckodriver
        )
    # # **********

    def tearDown(self):
        self.browser.quit()

    def test_new_visitor_path(self):
        # # Check if Django is working
        self.browser.get('http://localhost:8000')
        # self.browser.set_window_size(1024, 768)
        self.browser.maximize_window()
        self.assertIn('Pur Beurre', self.browser.title)

        # Visitor can search a product from navigation bar
        # or from page main search bar
        main_input_box = self.browser.find_element_by_id('nav_input_home')
        nav_input_box = self.browser.find_element_by_id('nav_input_base')
        # nav_input_box = WebDriverWait(self.browser, 10).until(
        #     EC.presence_of_element_located((By.ID, 'nav_input_base')))
        self.assertEqual(nav_input_box.get_attribute
                         ('placeholder'), 'Chercher')
        self.assertEqual(main_input_box.get_attribute
                         ('placeholder'), 'ex : Nutella')
        time.sleep(3)

        # Visitor type "Nutella" in search box
        main_input_box.send_keys('Nutella')
        main_input_box.send_keys(Keys.ENTER)
        time.sleep(10)

        # Check if Visitor succeed to reach products list page.
        products_list = self.browser.find_element_by_id('products_list')
        self.assertTrue(products_list)
        time.sleep(3)

        # Check if visitor can access to a product page
        product_page = \
            self.browser.find_element_by_link_text('Nutella')
        product_page.click()
        time.sleep(3)
        self.browser.back()
        time.sleep(3)

        # Check if visitor can access to subtitutes
        substitutes = \
            self.browser.find_element_by_link_text('Voir les subtituts')
        substitutes.click()
        time.sleep(3)
        self.browser.back()
        time.sleep(3)

        # Check if visitor can access to Open Food Facts link
        off_link = self.browser.find_element_by_link_text('-> Lien OFF <-')
        off_link.click()
        time.sleep(5)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
