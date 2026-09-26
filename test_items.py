import time

from selenium.webdriver.common.by import By


def test_guest_can_add_product_to_basket(browser):
    browser.get(
        "http://selenium1py.pythonanywhere.com/catalogue/"
        "coders-at-work_207/"
    )

    # Нужно для визуальной проверки языка страницы
    time.sleep(30)

    add_to_basket_button = browser.find_element(
        By.CSS_SELECTOR,
        "#add_to_basket_form button",
    )

    assert add_to_basket_button.is_displayed(), (
        "Кнопка добавления товара в корзину не отображается"
    )
