import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Edge(
        service=EdgeService(
            "C:/Users/localadmin/.cache/selenium/msedgedriver/"
            "win64/141.0.3537.71/msedgedriver.exe"))
    yield driver
    driver.quit()


def test_form(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/"
                "data-types.html")
    browser.find_element(By.NAME, "first-name").send_keys("Иван")
    browser.find_element(By.NAME, "last-name").send_keys("Петров")
    browser.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    browser.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    browser.find_element(By.NAME, "phone").send_keys("+7985899998787")
    browser.find_element(By.NAME, "zip-code").clear()
    browser.find_element(By.NAME, "city").send_keys("Москва")
    browser.find_element(By.NAME, "country").send_keys("Россия")
    browser.find_element(By.NAME, "job-position").send_keys("QA")
    browser.find_element(By.NAME, "company").send_keys("SkyPro")
    browser.find_element(By.CSS_SELECTOR,
                         ".btn.btn-outline-primary.mt-3").click()

    zip_code = browser.find_element(By.CSS_SELECTOR,
                                    ".alert.py-2.alert-danger")
    assert "alert-danger" in zip_code.get_attribute("class")

    fields = ["first-name", "last-name", "address", "e-mail",
              "phone", "city", "country", "job-position", "company"]
    for field in fields:
        element = browser.find_element(By.ID, field)
        assert "alert-success" in element.get_attribute("class")
