import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from conftest import driver



def test_task1(driver):
    """Тест проверяет отображение элементов на странице ITCareerHub."""

    def check_element(by, value, description):
        """Проверяет, отображается ли элемент, и выводит результат."""
        time.sleep(1)
        try:
            element = driver.find_element(by, value)
            assert element.is_displayed()
            print(f"✅ {description} найден")
        except NoSuchElementException:
            print(f"❌ {description} НЕ найден")
        except AssertionError:
            print(f"⚠️ {description} найден, но не отображается")

    # Проверка логотипа
    check_element(
        By.XPATH,
        '//*[@class="tn-atom__img t-img loaded"]', "Логотип ITCareerHub"
    )

    # Проверка ссылок в меню
    menu_links = [
        ("Программы", By.LINK_TEXT, "Ссылка 'Программы'"),
        ("Способы оплаты", By.LINK_TEXT, "Ссылка 'Способы оплаты'"),
        ("Новости", By.LINK_TEXT, "Ссылка 'Новости'"),
        ("О нас", By.LINK_TEXT, "Ссылка 'О нас'"),
        ("Отзывы", By.LINK_TEXT, "Ссылка 'Отзывы'"),
    ]

    for text, by, description in menu_links:
        check_element(by, text, description)

    # Проверка кнопок переключения языка
    check_element(By.CLASS_NAME, "tn-atom", "Кнопка переключения языка")



# 3. Кликнуть по иконке с телефонной трубкой
# 4. Проверить что текст “Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами” отображается.
def test_click_phone_icon(driver):
    time.sleep(2)
    phone_icon = driver.find_element(By.XPATH, "//img[@class='tn-atom__img t-img loaded']")
    phone_icon.click()

    time.sleep(1)

    # Проверяем наличие текста
    text_element = driver.find_element(
        By.XPATH,
        "//div[@field='tn_text_1711363912027']"
    )
    assert text_element
