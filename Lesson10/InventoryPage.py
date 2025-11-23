import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver


class InventoryPage:
    """
    Page Object для страницы каталога товаров (Inventory).
    """
    def __init__(self, browser: WebDriver):
        """
        Инициализация страницы каталога.
        :param browser: WebDriver — экземпляр браузера
        """
        self.browser = browser

    @allure.step("Добавить товар в корзину")
    def add_to_cart(self, item_id: str) -> None:
        """
        Добавляет товар в корзину по его идентификатору.
        :param item_id: str — идентификатор товара
        :return: None
        """
        self.browser.find_element(By.ID, item_id).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины.
        :return: None
        """
        self.browser.find_element(By.CSS_SELECTOR,
                                  ".shopping_cart_link").click()
