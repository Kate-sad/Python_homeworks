from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, browser):
        self.browser = browser

    def add_to_cart(self, item_id):
        self.browser.find_element(By.ID, item_id).click()

    def go_to_cart(self):
        self.browser.find_element(By.CSS_SELECTOR,
                                  ".shopping_cart_link").click()
