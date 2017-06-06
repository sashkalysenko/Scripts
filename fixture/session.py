class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        driver = self.app.wd
        self.app.open_home_page()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def logout(self):
        driver = self.app.wd
        driver.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        driver = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        driver = self.app.wd
        return len(driver.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        driver = self.app.wd
        return driver.find_element_by_xpath("//div/div[1]/form/b").text == "(" + username + ")"

    def ensure_login(self, username, password):
        driver = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
