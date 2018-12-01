
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

dr = webdriver.Chrome()
dr.implicitly_wait(3)
dr.get("http://google.com")

ac = webdriver.ActionChains(dr)
el = dr.find_element()
ac.move_to_element(el...)
