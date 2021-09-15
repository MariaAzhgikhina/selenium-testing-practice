import time
import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)
    
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

    browser.switch_to.alert.accept()
    
    x = int(browser.find_element_by_css_selector("#input_value").text)
    answer = calc(x)
    browser.find_element_by_css_selector("#answer").send_keys(answer)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
