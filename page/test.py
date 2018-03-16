from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
url = "http://testweb.runningdoctor.cn/"

driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_class_name("inputArea2").send_keys("18980944331")
driver.find_element_by_id("password").send_keys("18980944331")
driver.find_element_by_id("loginBtn").click()
WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath("//*[contains(text(),'四川大学华西第二医院')]")).click()
# driver.find_element_by_xpath("//*[contains(text(),'四川大学华西第二医院')]").click()