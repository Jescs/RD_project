# coding:utf-8
from selenium import webdriver
import unittest
from page.login_page import Login_page, Login_url


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.logindriver = Login_page(self.driver)
        self.driver.get(Login_url)

    def test_login1(self):
        self.logindriver.login("test", "111111")
        self.logindriver.is_login_sucess()

    def test_login2(self):
        self.logindriver.login("18980944331", "18980944331")
        self.logindriver.is_login_sucess()

    def test_login3(self):
        self.logindriver.login(" ", " ")
        self.logindriver.is_login_sucess()

    def test_login4(self):
        self.logindriver.login(",skdk1", " /jsjsjsj")
        self.logindriver.is_login_sucess()


if __name__ == '__main__':
    unittest.main(verbosity=2)
