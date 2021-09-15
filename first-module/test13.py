import time
import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    button = browser.find_element_by_css_selector("#button")
    button.click()
    #упадет с ошибкой тк элемент отсутстует

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()