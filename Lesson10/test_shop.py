import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from LoginPage import LoginPage
from InventoryPage import InventoryPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage


@pytest.fixture
def browser() -> webdriver.Firefox:
    """
    Фикстура для инициализации браузера Firefox.
    :return: webdriver.Firefox — экземпляр браузера
    """
    browser = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    yield browser
    browser.quit()


@allure.title("Полный сценарий покупки товаров")
@allure.description("Тест проверяет авторизацию, добавление товаров "
                    "в корзину, оформление заказа и итоговую сумму")
@allure.feature("Shop")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(browser: webdriver.Firefox) -> None:
    """
    Интеграционный тест: авторизация, добавление товаров в корзину,
    переход к оформлению заказа и проверка суммы.
    :param browser: webdriver.Firefox — экземпляр браузера
    :return: None
    """
    login_page = LoginPage(browser)
    with allure.step("Открыть страницу авторизации"):
        login_page.open()
    with allure.step("Выполнить вход в систему"):
        login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)

    with allure.step("Добавить товары в корзину"):
        inventory_page.add_to_cart("add-to-cart-sauce-labs-backpack")
        inventory_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
        inventory_page.add_to_cart("add-to-cart-sauce-labs-onesie")

    with allure.step("Перейти в корзину"):
        inventory_page.go_to_cart()

    cart_page = CartPage(browser)

    with allure.step("Перейти к оформлению заказа"):
        cart_page.checkout()

    checkout_page = CheckoutPage(browser)

    with allure.step("Заполнить форму оформления заказа"):
        checkout_page.fill_form("Katya", "Romashova", "Balashiha")

    with allure.step("Проверить итоговую сумму заказа"):
        total = checkout_page.get_total()
        assert "$58.29" in total
