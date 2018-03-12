Login_url = "http://testweb.runningdoctor.cn/"
from common.base import BasePage

class Login_page(BasePage):
    user_input = ("class name", "inputArea2")
    pwd_input = ("id", "password")
    login_button = ("id", "loginBtn")

    def input_user(self, username):
        self.send_keys(self.user_input, username)

    def input_pwd(self, pwd):
        self.send_keys(self.pwd_input, pwd)

    def click_login_button(self):
        self.click(self.login_button)

    def login(self, username, pwd):
        '''登录流程'''
        self.input_user(username)
        self.input_pwd(pwd)
        self.click_login_button()

    def is_login_sucess(self):
        # 判断是不是登录成功
        sucess_loc = ("class name", "topArea")
        result = self.is_text_in_element(sucess_loc,"选择要进入的组织")
        return result

if __name__ == "__main__":
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    login_driver = Login_page(driver)
    driver.get(Login_url)
    login_driver.login("18980944331","18980944331")
    time.sleep(3)
    login_driver.is_login_sucess()

