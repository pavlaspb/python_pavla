from selenium import webdriver
from fixture_contact.session import SessionHelper

class Application_contact:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)


    def return_to_contacts_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def create_new_contact(self, contact):
        wd = self.wd
        # init new contact creation
        wd.find_element_by_link_text("add new").click()
        # fill new contact form
        self.contact_filling(contact)
        # submit creation
        wd.find_element_by_xpath("(//input[@name='submit'])").click()

    def contact_filling(self, contact):
        wd = self.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def destroy(self):
        self.wd.quit()
