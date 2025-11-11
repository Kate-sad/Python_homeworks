from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, browser):
        self.browser = browser

    def fill_form(self, first_name, last_name, postal_code):
        self.browser.find_element(By.ID, "first-name").send_keys(first_name)
        self.browser.find_element(By.ID, "last-name").send_keys(last_name)
        self.browser.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.browser.find_element(By.ID, "continue").click()

    def get_total(self):
        return self.browser.find_element(By.CSS_SELECTOR,
                                         ".summary_total_label").text
