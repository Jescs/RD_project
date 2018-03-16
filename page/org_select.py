from page.login_page import Login_page, Login_url


class Org_select(Login_page):
    org_name = ("xpath", "//*[contains(text(),'四川大学华西第二医院')]")

    def orgselect(self):
        self.click(self.org_name)

    def is_selected_success(self):
        success_loc = ("class name", "tit")
        result = self.is_exists(success_loc)
        if result is True:
            result = self.get_text(success_loc)
            print(result)
        else:
            print("选择失败")


if __name__ == "__main__":
    from selenium import webdriver

    driver = webdriver.Chrome()
    login_driver = Org_select(driver)
    driver.get(Login_url)
    login_driver.login("18980944331", "18980944331")
    login_driver.orgselect()
    login_driver.is_login_sucess()