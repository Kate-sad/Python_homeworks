import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver


class LoginPage:
    """
    Page Object для страницы авторизации на сайте https://www.saucedemo.com/
    """

    def __init__(self, browser: WebDriver):
        """
        Инициализация страницы авторизации.
        :param browser: WebDriver — экземпляр браузера
        """
        self.browser = browser

    @allure.step("Открыть страницу авторизации")
    def open(self) -> None:
        """
        Открывает страницу авторизации.
        :return: None
        """
        self.browser.get("https://www.saucedemo.com/")

    @allure.step("Выполнить вход в систему")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему, заполняя поля логина и пароля.
        :param username: str — имя пользователя
        :param password: str — пароль пользователя
        :return: None
        """
        self.browser.find_element(By.ID, "user-name").send_keys(username)
        self.browser.find_element(By.ID, "password").send_keys(password)
        self.browser.find_element(By.ID, "login-button").click()
