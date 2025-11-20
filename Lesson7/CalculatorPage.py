from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/"
                         "slow-calculator.html")

    def set_delay(self, seconds):
        delay_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, value):
        button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{value}']"))
        )
        button.click()

    def get_result(self, expected_value, timeout=50):
        WebDriverWait(self.browser, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"),
                                             str(expected_value))
        )
        return self.browser.find_element(By.CSS_SELECTOR, ".screen").text
