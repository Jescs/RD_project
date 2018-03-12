# coding:utf-8
from selenium import webdriver
import unittest
from page.login_page import Login_page,Login_url


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver =webdriver.Chrome()
        self.logindriver = Login_page(self.driver)
        self.driver.get(Login_url)

    def test_login1(self):
        self.logindriver.login("test","111111")
        result = self.logindriver.is_login_sucess()
        print(result)

    def test_login2(self):
        self.logindriver.login("18980944331","18980944331")
        result = self.logindriver.is_login_sucess()
        print(result)

    def test_login3(self):
        self.logindriver.login(" "," ")
        result = self.logindriver.is_login_sucess()
        print(result)

    def test_login4(self):
        self.logindriver.login(",skdk1"," /jsjsjsj")
        result = self.logindriver.is_login_sucess()
        print(result)

if __name__ == '__main__':
    unittest.main(verbosity=2)

