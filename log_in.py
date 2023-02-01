from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.user_name_xpath = "//input[@name='username']"
        self.password_xpath = "//input[@name='password']"
        self.login_btn_xpath = "//input[@name='signon']"

    def user_name(self):
        self.driver.find_element(By.XPATH, self.user_name_xpath).send_keys("hariom123")

    def password(self):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys("hariom@123")

    def login_btn(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()
