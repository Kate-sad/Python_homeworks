import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Page Object для страницы калькулятора:
    https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
    """

    def __init__(self, browser):
        """
        Инициализация страницы калькулятора.
        :param browser: WebDriver — экземпляр браузера
        """
        self.browser = browser

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """
        Открываем страницу калькулятора.
        :return: None
        """
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/"
                         "slow-calculator.html")

    @allure.step("Установить задержку выполнения")
    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку выполнения операций калькулятора.
        :param seconds: int — количество секунд задержки
        :return: None
        """
        delay_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    @allure.step("Нажать кнопку калькулятора")
    def click_button(self, value: str) -> None:
        """
        Нажимает кнопку калькулятора по её значению.
        :param value: str — значение кнопки
        :return: None
        """
        button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{value}']"))
        )
        button.click()

    @allure.step("Получить результат вычисления")
    def get_result(self, expected_value: str, timeout: int = 50) -> str:
        """
        Получает результат вычисления с экрана калькулятора.
        :param expected_value: str — ожидаемое значение результата
        :param timeout: int — время ожидания результата
        :return: str — текст результата с экрана
        """
        WebDriverWait(self.browser, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"),
                                             str(expected_value))
        )
        return self.browser.find_element(By.CSS_SELECTOR, ".screen").text
