import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select



try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)
    summa = int(browser.find_element_by_css_selector("#num1").text) + int(browser.find_element_by_css_selector("#num2").text)

    browser.find_element_by_css_selector("select").click()
    select = Select(browser.find_element_by_css_selector("select"))
    select.select_by_value(str(summa))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
