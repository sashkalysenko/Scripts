from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        driver = self.wd
        driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
