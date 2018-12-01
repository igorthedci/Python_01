from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("http://google.com")

# search_field = driver.find_element_by_name("q")
# search_field.send_keys("Python")
# search_field.send_keys(Keys.CONTROL, "t")

print(driver.window_handles)
print(driver.current_window_handle)

original_window = driver.current_window_handle

ac = webdriver.ActionChains(driver)
els = driver.find_elements_by_css_selector(".fbar span a")
ac.key_down(Keys.CONTROL).click(els[0]).perform()
new_window = driver.window_handles[-1]

print("driver.window_handles", driver.window_handles)
print(driver.current_window_handle)

# all_windows = driver.window_handles
# this_window  = driver.current_window_handle

driver.switch_to.window(new_window)
time.sleep(8)
driver.close()
driver.switch_to.window(original_window)
# driver.close()

