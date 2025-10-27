from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

browser.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
element = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.ID, "landscape")))
print(browser.find_element(By.ID, "award").get_attribute("src"))
browser.quit()
