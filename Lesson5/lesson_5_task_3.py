from selenium import webdriver
from selenium.webdriver.common.by import By

driwer = webdriver.Firefox()
driwer.get("http://the-internet.herokuapp.com/inputs")
search_input = driwer.find_element(By.CSS_SELECTOR, "input")
search_input.send_keys("Sky")
search_input.clear()
search_input.send_keys("Pro")
driwer.quit()
