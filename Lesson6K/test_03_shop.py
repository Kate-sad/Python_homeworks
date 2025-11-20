import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()


def test_shop(browser):
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    browser.find_element(By.CSS_SELECTOR,
                         ".shopping_cart_link").click()
    browser.find_element(By.ID, "checkout").click()
    browser.find_element(By.ID, "first-name").send_keys("Katya")
    browser.find_element(By.ID, "last-name").send_keys("Romashova")
    browser.find_element(By.ID, "postal-code").send_keys("Balashiha")
    browser.find_element(By.ID, "continue").click()
    total = browser.find_element(By.CSS_SELECTOR, ".summary_total_label").text

    assert "$58.29" in total
