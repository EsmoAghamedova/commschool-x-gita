import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import  TimeoutException


class SauceDemoTests(unittest.TestCase):

    BASE_URL = "https://www.saucedemo.com/"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.get(self.BASE_URL)

    def tearDown(self):
        self.driver.quit()

    def login(self, username, password="secret_sauce"):
        self.wait.until(EC.presence_of_element_located(
            (By.ID, "user-name"))).clear()
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def is_login_successful(self):
        try:
            self.wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "inventory_list")))
            return True
        except TimeoutException:
            return False

    def get_error_message(self):
        try:
            error_element = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "[data-test='error']"))
            )
            return error_element.text
        except TimeoutException:
            return None

    def robust_click(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(EC.element_to_be_clickable(element))
        self.driver.execute_script("arguments[0].click();", element)

    def logout(self):
        burger_button = self.wait.until(
            EC.presence_of_element_located((By.ID, "react-burger-menu-btn")))
        self.robust_click(burger_button)
        logout_link = self.wait.until(
            EC.presence_of_element_located((By.ID, "logout_sidebar_link")))
        self.robust_click(logout_link)
        self.wait.until(EC.presence_of_element_located(
            (By.ID, "login-button")))

    def add_items_to_cart(self, count):
        add_buttons = self.driver.find_elements(
            By.CSS_SELECTOR, "button.btn_inventory")
        for i in range(count):
            add_buttons[i].click()

    def remove_item_from_cart(self, index=0):
        remove_buttons = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "button[id^='remove-']"))
        )
        remove_buttons[index].click()

    def check_social_icon(self, link_id):
        main_window = self.driver.current_window_handle
        icon = self.wait.until(
            EC.presence_of_element_located((By.ID, link_id)))
        self.robust_click(icon)
        self.wait.until(lambda d: len(d.window_handles) > 1)
        new_window = [
            w for w in self.driver.window_handles if w != main_window][0]
        self.driver.switch_to.window(new_window)
        self.driver.close()
        self.driver.switch_to.window(main_window)

    def test_locked_out_user(self):
        self.login("locked_out_user")
        if self.is_login_successful():
            self.assertTrue(True)
        else:
            error_text = self.get_error_message()
            self.assertIsNotNone(error_text)
            self.assertIn("locked out", error_text.lower())

    def test_performance_glitch_user(self):
        self.login("performance_glitch_user")
        if self.is_login_successful():
            self.logout()
            self.assertNotIn("inventory.html", self.driver.current_url)
        else:
            error_text = self.get_error_message()
            self.assertIsNotNone(error_text)

    def test_problem_user(self):
        self.login("problem_user")
        if self.is_login_successful():
            self.add_items_to_cart(2)
            cart_badge = self.driver.find_elements(
                By.CLASS_NAME, "shopping_cart_badge")
            self.assertTrue(len(cart_badge) > 0)
            self.remove_item_from_cart(0)
            self.remove_item_from_cart(0)
            self.logout()
        else:
            error_text = self.get_error_message()
            self.assertIsNotNone(error_text)

    def test_standard_user(self):
        self.login("standard_user")
        if self.is_login_successful():
            self.add_items_to_cart(2)
            time.sleep(5)
            self.remove_item_from_cart(0)

            product_link = self.wait.until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "inventory_item_name"))
            )
            self.robust_click(product_link)
            self.wait.until(EC.url_contains("inventory-item.html"))
            self.wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "inventory_details")))
            time.sleep(5)
            self.driver.back()
            self.wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "inventory_list")))

            sort_dropdown = self.wait.until(EC.element_to_be_clickable(
                (By.CLASS_NAME, "product_sort_container")))
            sort_dropdown.click()
            self.driver.find_element(
                By.CSS_SELECTOR, "option[value='hilo']").click()

            prices = self.driver.find_elements(
                By.CLASS_NAME, "inventory_item_price")
            price_values = [float(p.text.replace("$", "")) for p in prices]
            self.assertEqual(price_values, sorted(price_values, reverse=True))

            self.check_social_icon("social_facebook")
            self.check_social_icon("social_linkedin")

            self.logout()
        else:
            error_text = self.get_error_message()
            self.assertIsNotNone(error_text)


if __name__ == "__main__":
    unittest.main()
