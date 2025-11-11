import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from LoginPage import LoginPage
from InventoryPage import InventoryPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage


@pytest.fixture
def browser():
    browser = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    yield browser
    browser.quit()


def test_shop(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.add_to_cart("add-to-cart-sauce-labs-backpack")
    inventory_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    inventory_page.add_to_cart("add-to-cart-sauce-labs-onesie")
    inventory_page.go_to_cart()

    cart_page = CartPage(browser)
    cart_page.checkout()

    checkout_page = CheckoutPage(browser)
    checkout_page.fill_form("Katya", "Romashova", "Balashiha")
    total = checkout_page.get_total()

    assert "$58.29" in total
