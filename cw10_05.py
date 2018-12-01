from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

base_url = "http://127.0.0.1/oxwall"

# TOP NAVIGATOR
signin_button = (By.CSS_SELECTOR, "span.ow_signin_label")
user_profile_icon = (By.XPATH, "//div[contains(@class,'ow_console_dropdown_hover')]")
user_menu_signout = (By.XPATH, "//div[@class='ow_console_dropdown_cont']/a")

# SIGN IN POPUP
signin_title = (By.XPATH, "//h3[@class='ow_ic_file']")
signin_name_field = (By.XPATH, "//*[@class='ow_user_name']/input")
signin_password_field = (By.XPATH, "//*[@class='ow_password']/input")
signin_remember_checkbox = (By.XPATH, "//*[@name='remember']")
signin_signin_button = (By.XPATH, "//span[@class=' ow_positive']")

# NEWS
news_input = (By.XPATH, "//textarea[@name='status']")
news_input_submit = (By.XPATH, "//input[@name='save']")
news_content = (By.XPATH, "//div[contains(@class,'ow_newsfeed_content')]")


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
    time.sleep(2)

    print("Looking the newsfeed for new text...", end='')
    elements = wd.find_elements(*news_content)

    for element in elements:
        if my_news in element.text:
            print('PASS')
            break
    else:
        print('FAIL')


def user_signout():
    elements = wd.find_elements(*user_profile_icon)
    element = elements[0]  # user icon is #0
    mouse_cursor = ActionChains(wd)
    mouse_cursor.move_to_element(element).perform()
    time.sleep(2)

    elements = wd.find_elements(*user_menu_signout)
    element = elements[5]
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

    user_signout()

    wd.close()

