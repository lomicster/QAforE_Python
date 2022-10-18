#Selenium installation
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/cats.html')
time.sleep(5)
bullet_cat = driver.find_element(By.XPATH, "/html/body/main/div/div/div/div[1]/div/div/div/div/button[1]").click
time.sleep(5)

"""HW:
6.1. Найдите кпопку c текстом "Gold". Попробуйте подобрать как минимум 2 разных XPATH и/или CSS-селекторов
http://suninjuly.github.io/xpath_examples

/html/body/div[2]/button[3]
//div/button[3]
//button[text()='Gold']

body > div:nth-child(2) > button:nth-child(3)

6.2. Найдите элемент с текстом "Lenin cat". Чем больше разных XPATH и/или CSS-селекторов сможете подобрать, тем лучше
http://suninjuly.github.io/cats.html"""

#politic
//*[@id="politic"]
/html/body/main/div/div/div/div[3]/div/div/p