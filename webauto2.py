#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
driver.get('http://www.skillrack.com/faces/ui/profile.xhtml')
search=driver.find_element_by_xpath('//*[@id="input_j_id_s"]')
search.send_keys("e8ec064@sairamce")
passw=driver.find_element_by_xpath('//*[@id="input_j_id_u"]')
passw.send_keys("dharun")
search.send_keys(Keys.ENTER)