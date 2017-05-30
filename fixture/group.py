class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        driver = self.app.wd
        driver.find_element_by_link_text("group page").click()

    def create(self, group):
        driver = self.app.wd
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
        driver = self.app.wd
        driver.find_element_by_link_text("groups").click()
