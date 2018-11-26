from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
# import time

search_url = "https://duckduckgo.com/"
base_url = "http://automationpractice.com"

# Navigation locators
logo_loc = "img.logo"
search_loc = "input.search_query"
lens_loc = "button.button-search"
cart_loc = "div.shopping_cart a"
cat1_loc = "a[title='Women']"  # WOMEN
cat2_loc = "a[title='Dresses']"  # DRESSES
cat3_loc = "a[title='T-shirts']"  # T-SHIRTS

# driver = webdriver.Edge()
# driver.implicitly_wait(30)
wd = webdriver.Edge()
# wd = webdriver.Firefox()
wd.implicitly_wait(3)


def open_main_page():
    wd.get(base_url)
# wd.maximize_window()
# time.sleep(2)
# wd.minimize_window()


def is_element_present(driver, by, locator):
    try:
        element = driver.find_element(by, locator)
    except NoSuchElementException:
        return False
    return element


def type_search(search_text):
    open_main_page()
    element = is_element_present(wd, By.CSS_SELECTOR, search_loc)
    if element:
        element.clear()
        element.send_keys(search_text)
        button = is_element_present(wd, By.CSS_SELECTOR, lens_loc)
        button.click()


def open_cart():
    element = is_element_present(wd, By.CSS_SELECTOR, cart_loc)
    if element:
        assert 'Cart' in element.text
        element.click()


def open_women_popup():
    element = is_element_present(wd, By.CSS_SELECTOR, cat1_loc)
    if element:
        action = webdriver.ActionChains(wd)



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
