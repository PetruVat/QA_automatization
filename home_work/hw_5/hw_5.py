import time
from conftest import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains




def test_iframe_text(driver):
     driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
     time.sleep(3)

     iframe = driver.find_element(By.ID, "my-iframe")
     driver.switch_to.frame(iframe)

     paragraphs = driver.find_elements(By.TAG_NAME, "p")

     expected_text = "semper posuere integer et senectus justo curabitur."

     found = any(expected_text in p.text for p in paragraphs)

     assert found, "Текст не найден в iframe"

     print("\n Тест пройден: текст найден в iframe")




def test_task2(driver):
     driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
     time.sleep(3)

     iframe = driver.find_element(By.TAG_NAME, "iframe")
     driver.switch_to.frame(iframe)

     photo = driver.find_element(By.XPATH, "//ul[@id='gallery']/li[1]")
     trash = driver.find_element(By.ID, "trash")

     actions = ActionChains(driver)
     actions.drag_and_drop(photo, trash).perform()
     time.sleep(2)

     photos_in_trash = len(driver.find_elements(By.XPATH, "//div[@id='trash']/ul/li"))
     photos_in_gallery = len(driver.find_elements(By.XPATH, "//ul[@id='gallery']/li"))

     assert photos_in_trash == 1, "Ошибка: В корзине нет фотографий!"
     assert photos_in_gallery == 3, "Ошибка: В основной области осталось не 3 фотографии!"
     print("Тест успешно пройден: Фотография перемещена в корзину, в галерее осталось 3 фотографии.")