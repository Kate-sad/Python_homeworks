import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver


class CheckoutPage:
    """
    Page Object для страницы оформления заказа.
    """
    def __init__(self, browser: WebDriver):
        """
        Инициализация страницы оформления заказа.
        :param browser: WebDriver — экземпляр браузера
        """
        self.browser = browser

    @allure.step("Заполнить форму оформления заказа")
    def fill_form(self, first_name: str, last_name: str,
                  postal_code: str) -> None:
        """
        Заполняет форму оформления заказа и нажимает кнопку 'Continue'.
        :param first_name: str — имя покупателя
        :param last_name: str — фамилия покупателя
        :param postal_code: str — почтовый индекс
        :return: None
        """
        self.browser.find_element(By.ID, "first-name").send_keys(first_name)
        self.browser.find_element(By.ID, "last-name").send_keys(last_name)
        self.browser.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.browser.find_element(By.ID, "continue").click()

    @allure.step("Получить итоговую сумму заказа")
    def get_total(self) -> str:
        """
        Получает итоговую сумму заказа со страницы.
        :return: str — текстовое значение итоговой суммы
        """
        return self.browser.find_element(By.CSS_SELECTOR,
                                         ".summary_total_label").text
