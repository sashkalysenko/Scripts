from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fixture.session import SessionHelper

class Application():
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def return_to_groups_page(self):
        driver = self.wd
        driver.find_element_by_link_text("group page").click()

    def create_group(self, group):
        driver = self.wd
        # open groups page
        self.open_groups_page()
        # init group creation
        driver.find_element_by_name("new").click()
        # fill group form
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        driver.find_element_by_name("submit").click()
        # return to groups page
        self.return_to_groups_page()

    def open_groups_page(self):
        driver = self.wd
        driver.find_element_by_link_text("groups").click()

    def open_home_page(self):
        driver = self.wd
        driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
