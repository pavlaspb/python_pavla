class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, login, password):
        wd = self.app.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()


    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()