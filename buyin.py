from selenium.webdriver.common.by import By


class Buy:
    def __init__(self, driver):
        self.driver = driver
        self.fish_xpath = "//img[@src='../images/fish_icon.gif']"
        self.product_id_xpath = "//a[normalize-space()='FI-SW-01']"
        self.add_cart1_xpath = "//tbody/tr[2]/td[5]/a[1]"
        self.checkout_btn_xpath = "//a[normalize-space()='Proceed to Checkout']"

    def fish_btn(self):
        self.driver.find_element(By.XPATH, self.fish_xpath).click()

    def product_id(self):
        self.driver.find_element(By.XPATH, self.product_id_xpath).click()

    def cart(self):
        self.driver.find_element(By.XPATH, self.add_cart1_xpath).click()

    def checkout(self):
        self.driver.find_element(By.XPATH, self.checkout_btn_xpath).click()
