import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import CalculatorPage


@pytest.fixture
def browser():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()


def test_calc(browser):
    calc_page = CalculatorPage(browser)
    calc_page.open()
    calc_page.set_delay(45)

    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    result = calc_page.get_result(15, timeout=50)
    assert result == "15"
