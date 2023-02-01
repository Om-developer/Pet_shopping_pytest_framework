import pytest


from test_1.log_in import Login
from test_1.Loger import logclass
from test_1.buyin import Buy


@pytest.mark.usefixtures("setup")
class Test(logclass):
    def test_001(self):
        log = self.getthelogs()
        by = Buy(self.driver)
        lg = Login(self.driver)
        by.fish_btn()
        log.info("fish button clicked")
        by.product_id()
        log.info("product id clicked")
        by.cart()
        log.info("cart has been clicked successfully")
        by.checkout()
        log.info("checkout button clicked")
        lg.user_name()
        log.info("user name inputted successfully")
        lg.password()
        log.info("password filled successfully")
        lg.login_btn()
        log.info("login has been done successfully")



