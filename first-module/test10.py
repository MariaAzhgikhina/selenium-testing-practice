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
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)
    
    browser.find_element_by_css_selector("[name='firstname']").send_keys("[name='firstname']")
    browser.find_element_by_css_selector("[name='lastname']").send_keys("[name='lastname']")
    browser.find_element_by_css_selector("[name='email']").send_keys("[name='email']")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')   
    browser.find_element_by_css_selector("[type='file']").send_keys(file_path)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
