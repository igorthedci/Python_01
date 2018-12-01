from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
import time
import requests

base_url = "http://127.0.0.1/oxwall"

# Navigation locators
signin_button = (By.CSS_SELECTOR, "span.ow_signin_label")
user_profile_icon = (By.XPATH, "//div[contains(@class,'ow_console_dropdown_hover')]")

# search_loc = "search_query_top"
# lens_loc = "button.button-search"
# cart_loc = "div.shopping_cart a"

# breadcrumb_search_loc = "div.breadcrumb span[title='Search']"
#
# cat1_women_loc = "a[title='Women']"  # WOMEN
# cat1_dresses_loc = "a[title='Dresses']"  # DRESSES
# cat1_tshirts_loc = "a[title='T-shirts']"  # T-SHIRTS
# cat2_tops_loc = "a.sf-with-ul[title='Tops']"  # WOMEN > TOPS
# cat2_dresses_loc = "a.sf-with-ul[title='Dresses']"  # WOMEN > DRESSES
# cat3_tshirts_loc = "a[title='T-shirts']"

signin_title = (By.XPATH, "//h3[@class='ow_ic_file']")
signin_name_field = (By.XPATH, "//*[@class='ow_user_name']/input")
signin_password_field = (By.XPATH, "//*[@class='ow_password']/input")
signin_remember_checkbox = (By.XPATH, "//*[@name='remember']")
signin_signin_button = (By.XPATH, "//span[@class=' ow_positive']")


# Search locators
# search_string = "top"
# search_title_loc = "h1.page-heading"
# search_token_loc = "span.navigation_page"
# search_counter_loc = "span.heading-counter"
# negative_search_loc = "span.lighter"
# positive_search_loc = "p.alert.alert-warning"


news_input = (By.XPATH, "//textarea[@name='status']")
news_input_submit = (By.XPATH, "//input[@name='save']")


def open_main_page():
    wd.get(base_url)
    expected_title = "Oxwall - Find New Friends Here!"
    assert expected_title in wd.title


def open_signin_page():
    element = wd.find_element(*signin_button)
    element.click()
    element = wd.find_element(*signin_title)
    expected_title = "Please sign in"
    assert expected_title in element.text


def type_signin_kreds():
    element = wd.find_element(*signin_name_field)
    element.clear()
    element.send_keys("admin")

    element = wd.find_element(*signin_password_field)
    element.clear()
    element.send_keys("Adm1n")

    element = wd.find_element(*signin_remember_checkbox)
    if element.get_attribute("checked"):
        element.click()

    element = wd.find_element(*signin_signin_button)
    element.click()

    elements = wd.find_elements(*user_profile_icon)
    print(elements)


def type_news_feed(my_news):
    element = wd.find_element(*news_input)
    element.clear()
    element.send_keys(my_news)
    element = wd.find_element(*news_input_submit)
    element.click()



if __name__ == '__main__':

    wd = webdriver.Chrome()
    # wd = webdriver.Edge()
    # wd = webdriver.Firefox()

    wd.implicitly_wait(5)

    open_main_page()  # Test the main page

    open_signin_page()
    type_signin_kreds()

    type_news_feed("its my news")

    # wd.close()

