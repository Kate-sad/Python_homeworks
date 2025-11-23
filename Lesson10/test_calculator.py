import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import CalculatorPage


@pytest.fixture
def browser() -> webdriver.Chrome:
    """
    Фикстура для инициализации браузера Chrome.
    :return: webdriver.Chrome — экземпляр браузера
    """
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()


@allure.title("Проверка сложения чисел 7 + 8 = 15")
@allure.description("Тест проверяет корректность работы калькулятора"
                    " при сложении 7 и 8")
@allure.feature("Calculator")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc(browser: webdriver.Chrome) -> None:
    """
    Тест проверяет корректность сложения чисел 7 и 8.
    :param browser: webdriver.Chrome — экземпляр браузера
    :return: None
    """
    calc_page = CalculatorPage(browser)
    with allure.step("Открыть страницу калькулятора"):
        calc_page.open()
    with allure.step("Установить задержку 45 секунд"):
        calc_page.set_delay(45)
    with allure.step("Выполнить операцию 7 + 8 ="):
        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")
    with allure.step("Проверить результат"):
        result = calc_page.get_result(15, timeout=50)
        assert result == "15"
