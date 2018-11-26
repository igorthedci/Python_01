from selenium import webdriver
import time

search_url = "https://duckduckgo.com/"

# driver = webdriver.Firefox()
# driver.get(search_url)
# driver.close()
#
# driver = webdriver.Chrome()
# driver.get(search_url)
# driver.close()

# driver = webdriver.Ie()
# driver.implicitly_wait(30)
# driver.get(search_url)
# driver.close()

# driver = webdriver.Remote(
#     desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
#     command_executor="http://127.0.0.1:4444/wd/hub"
# )
# driver.implicitly_wait(30)
# driver.get(search_url)
# driver.maximize_window()
# time.sleep(2)
# driver.minimize_window()
# time.sleep(1)
# driver.close()

driver = webdriver.Edge()
driver.implicitly_wait(30)
driver.get(search_url)
driver.close()
