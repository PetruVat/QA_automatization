import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from conftest import driver



# def test_text_input(driver):
#     driver.get("http://uitestingplayground.com/textinput")
#     text_field = driver.find_element(By.CLASS_NAME, "form-control")
#     text_field.click()
#     text_field.send_keys("ITCH")
#     execute_button = driver.find_element(By.CLASS_NAME, "btn-primary")
#     execute_button.click()
#
#     assert execute_button.text == "ITCH", "Тест не прошел"


# def test_check_image(driver):
#     driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
#     time.sleep(10)
#     image_locator = driver.find_element(By.XPATH, '//img[@alt="award"]')
#     assert image_locator.get_attribute("alt") == "award"