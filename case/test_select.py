from selenium import webdriver
from page.org_select import Org_select
from page.login_page import Login_page, Login_url
import unittest

class Test_select(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.logindriver = Org_select(self.driver)
        self.driver.get(Login_url)
        self.logindriver.login("18980944331","18980944331")

    def test_select(self):
        self.logindriver.orgselect()


if __name__=="__main__":
    unittest.main(verbosity=2)