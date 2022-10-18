#Selenium installation
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/cats.html')
time.sleep(5)
bullet_cat = driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[1]/div/div/div/div/button[1]").click
time.sleep(5)
