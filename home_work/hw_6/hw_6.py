from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# 🔐 LoginPage
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()


# 🛒 ProductsPage
class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name):
        xpath = f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
        self.driver.find_element(By.XPATH, xpath).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


# 🧺 CartPage
class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()


# 📋 CheckoutPage
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_user_info(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self):
        total_element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        return total_text.replace("Total: $", "")


# 🚀 Основной тест
def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    try:
        # Login
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Add products
        products_page = ProductsPage(driver)
        products = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
        for product in products:
            products_page.add_product_to_cart(product)
        products_page.go_to_cart()

        # Checkout
        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_user_info("John", "Doe", "12345")

        total = checkout_page.get_total()
        print(f"Итоговая сумма: ${total}")
        assert total == "58.29", f"❌ Итоговая сумма {total}, ожидалось 58.29"
        print("✅ Тест успешно пройден!")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
