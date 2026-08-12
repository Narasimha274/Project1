from selenium.webdriver.common.by import By

class LoginPage:

    txt_username = (By.ID, "user-name")
    txt_password = (By.ID, "password")
    btn_login = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.txt_username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.txt_password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.btn_login).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()