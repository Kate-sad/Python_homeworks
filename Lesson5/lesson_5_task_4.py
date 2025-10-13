from selenium import webdriver
from selenium.webdriver.common.by import By

driwer = webdriver.Firefox()
driwer.get("http://the-internet.herokuapp.com/login")
username_input = driwer.find_element(By.ID, "username")
username_input.send_keys("tomsmith")
password_input = driwer.find_element(By.ID, "password")
password_input.send_keys("SuperSecretPassword!")
driwer.find_element(By.CSS_SELECTOR, ".radius").click()
text = driwer.find_element(By.ID, "flash").text
print(text)
driwer.quit()
