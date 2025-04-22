from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://itcareerhub.de/ru")
about_link = driver.find_element(By.LINK_TEXT, 'Способы оплаты')
about_link.click()
time.sleep(3)
driver.save_screenshot('./screens/2.png')
driver.quit()