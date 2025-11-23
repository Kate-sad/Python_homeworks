import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver


class CartPage:
    """
    Page Object для страницы корзины интернет-магазина.
    """
    def __init__(self, browser: WebDriver):
        """
        Инициализация страницы корзины.
        :param browser: WebDriver — экземпляр браузера
        """
        self.browser = browser

    @allure.step("Перейти к оформлению заказа")
    def checkout(self) -> None:
        """
        Нажимает кнопку 'Checkout' для перехода к оформлению заказа.
        :return: None
        """
        self.browser.find_element(By.ID, "checkout").click()
