from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("http://google.com")


for i in range(10):
    try:
        if len(driver.find_elements_by_class_name("ow_console_item")) == 3:
            break
    except:
        pass
    time.sleep(1)
else:
    raise TimeoutException("No found such amount of elements")


def presents_of_three_elements(driver):
    buttons = driver.find_elements_by_class_name("ow")
    if len(buttons) == 3:
        return buttons


wait = WebDriverWait(driver, 10)
x = wait.until(presents_of_three_elements)

x = wait.until(lambda driver: len(driver.find_elements_by_class_name("ow_console_item")) == 3)
