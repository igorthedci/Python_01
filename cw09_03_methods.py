from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
import time
import requests

search_url = "https://duckduckgo.com/"
base_url = "http://automationpractice.com"

# Navigation locators
logo_loc = "img.logo"
search_loc = "search_query_top"
lens_loc = "button.button-search"
cart_loc = "div.shopping_cart a"

breadcrumb_search_loc = "div.breadcrumb span[title='Search']"

cat1_women_loc = "a[title='Women']"  # WOMEN
cat1_dresses_loc = "a[title='Dresses']"  # DRESSES
cat1_tshirts_loc = "a[title='T-shirts']"  # T-SHIRTS
cat2_tops_loc = "a.sf-with-ul[title='Tops']"  # WOMEN > TOPS
cat2_dresses_loc = "a.sf-with-ul[title='Dresses']"  # WOMEN > DRESSES
cat3_tshirts_loc = "a[title='T-shirts']"

# Search locators
search_string = "top"
search_title_loc = "h1.page-heading"
search_token_loc = "span.navigation_page"
search_counter_loc = "span.heading-counter"
negative_search_loc = "span.lighter"
positive_search_loc = "p.alert.alert-warning"


def log_print(values):
    print(values, end=' ')
    yield
    print(values)


def is_element_present(driver, by, locator):
    try:
        log_print("Looking for {} locator {}".format(by, locator))
        element = driver.find_element(by, locator)
    except NoSuchElementException:
        log_print("FAIL")
        return False
    log_print("PASS")
    return element


def open_main_page():
    wd.get(base_url)
    print("The home page has title", wd.title)
    assert wd.title == "My Store"


def type_search_text(search_text):
    open_main_page()
    element = is_element_present(wd, By.ID, search_loc)
    print("Looking for the Search title:", "PASS" if element else "FAIL")
    if element:
        element.clear()
        element.send_keys(search_text)
        button = is_element_present(wd, By.CSS_SELECTOR, lens_loc)
        print("Looking for the Lens button:", "PASS" if button else "FAIL")
        button.click()


def test_search_result(search_string):
    print("Search string: {}. Testing result page".format(search_string))
    print("Looking for 'Search' in the title:", "PASS" if 'Search' in wd.title else "FAIL")
#
    element = is_element_present(wd, By.CSS_SELECTOR, breadcrumb_search_loc)
    print("Looking for the Search breadcrumb:", "PASS" if element else "FAIL")
#
    element = is_element_present(wd, By.CSS_SELECTOR, search_loc)
    print("Looking for 'Search' in the title:", "PASS" if 'Search' in wd.title else "FAIL")
    if element:
        # assert "Search" in element.text
        print("Found an element with text ({})".format(element.text))
        element = is_element_present(wd, By.CSS_SELECTOR, search_counter_loc)
        num_items = int(element.text.split()[0])
        print("The number of found items is {}".format(num_items))
        # if num_items:  # results are/greater 1
        #     element = is_element_present(wd, By.CSS_SELECTOR, positive_search_loc)))
        # else  # result = 0
        #     element = is_element_present(wd, By.CSS_SELECTOR, negative_search_loc)))


# def open_cart():
#     element = is_element_present(wd, By.CSS_SELECTOR, cart_loc)
#     if element:
#         assert 'Cart' in element.text
#         element.click(2)


def open_women_popup():
    element = is_element_present(wd, By.CSS_SELECTOR, cat1_women_loc)
    if element:
        mouse = ActionChains(wd)
        mouse.move_to_element(element).perform()
        # test_women_popup()
        # time.sleep(2)
        popup = is_element_present(wd, By.CSS_SELECTOR,
                                   cat1_women_loc+" [style='display: block;']")  # wait for the popup
    return element


def test_women_popup():
    element = open_women_popup()
    if not is_hrefs_200(element):
        return False
    if element:
        sub_el = test_link_200(wd, By.CSS_SELECTOR, cat2_tops_loc)
        sub_el = test_link_200(wd, By.CSS_SELECTOR, cat2_dresses_loc)
        sub_el = is_element_present(wd, By.CSS_SELECTOR, cat2_tops_loc)
        if sub_el == False:
            return False

        sub_link = sub_el.get_attribute("href")
        response = requests.get(sub_link)
        assert response.status_code == 200
        sub_el = is_element_present(wd, By.CSS_SELECTOR, cat2_dresses_loc)
        if sub_el == False:
            return False
    return element


def test_link_200(driver, by, locator):
    element = is_element_present(driver, by, locator)
    if element:
        href_link = element.get_attribute("href")
        response = requests.head(href_link)
        print("Test link: {} Status: {}".format(href_link, response.status_code))
        if response.status_code != 200:
            return False
    return element


def is_hrefs_200(element):
    if element:
        href_elements = element.find_elements(By.CSS_SELECTOR, " [href='*']")  # loop with all href-heirs
        for href in href_elements:
            link = href.get_attribute("href")
            response = requests.head(link)
            print("Test link: {} Status: {}".format(link, response.status_code))
            if response.status_code != 200:  # is the link vital
                return False
    return True


if __name__ == '__main__':

    # driver = webdriver.Edge()
    # driver.implicitly_wait(30)
    wd = webdriver.Edge()
    # wd = webdriver.Firefox()

    wd.implicitly_wait(3)

    open_main_page()  # Test the main page

    type_search_text(search_string)  # Test the search method
    test_search_result(search_string)

    open_women_popup()
    test_women_popup()

    wd.close()

