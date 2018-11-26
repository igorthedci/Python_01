from selenium import webdriver
from selenium.webdriver.common.by import By
# import time

search_url = "https://duckduckgo.com/"

# driver = webdriver.Edge()
# driver.implicitly_wait(30)
wd = webdriver.Edge()
# wd = webdriver.Firefox()
wd.implicitly_wait(30)

wd.get(search_url)
# wd.maximize_window()
# time.sleep(2)
# wd.minimize_window()

elements = wd.find_elements(By.ID, "wedonttrack")
print("By.ID wedonttrack = {}".format(len(elements)))
elements = wd.find_elements_by_id("wedonttrack")
print("by_id wedonttrack = {}".format(len(elements)))

elements = wd.find_elements(By.NAME, "q")
print("By.NAME q = {}".format(len(elements)))
elements = wd.find_elements_by_name("q")
print("by_name q = {}".format(len(elements)))

tmp_class_name = "js-onboarding-ed-arrow"
elements = wd.find_elements_by_class_name(tmp_class_name)
print("by_class_name {} = {}".format(tmp_class_name, len(elements)))
elements = wd.find_elements(By.CLASS_NAME, tmp_class_name)
print("by.CLASS_NAME {} = {}".format(tmp_class_name, len(elements)))

tmp_css = "span.js-onboarding-ed-back-to-search"
elements = wd.find_elements(By.CSS_SELECTOR, tmp_css)
print("By.CSS_SELECTOR {} = {}, text = {}".format(tmp_css, len(elements), elements[0].text))
elements = wd.find_elements_by_css_selector(tmp_css)
print("by.CLASS_NAME {} = {}, text = {}".format(tmp_css, len(elements), elements[0].text))

# elements = wd.find_elements_by_link_text()

elements = wd.find_elements(By.PARTIAL_LINK_TEXT, "DuckDuckGo")
print("By.PARTIAL_LINK_TEXT DucDuckGo = {}".format(len(elements)))
elements = wd.find_elements_by_partial_link_text("DuckDuckGo")
print("by_partial_link_text DucDuckGo = {}".format(len(elements)))

# elements = wd.find_elements_by_tag_name()

tmp_xpath = "//*[contains(@class,'js-onboarding-ed-dismiss')]"
elements = wd.find_elements_by_xpath(tmp_xpath)
print("by_xpath {} = {}".format(tmp_xpath, len(elements)))
elements = wd.find_elements(By.XPATH, tmp_xpath)
print("By.XPATH {} = {}".format(tmp_xpath, len(elements)))


wd.close()
