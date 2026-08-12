from pages.login_page import LoginPage
from utilities.read_config import ReadConfig

class TestLogin:

    def test_login(self, driver):

        driver.get(ReadConfig.get_url())

        login = LoginPage(driver)

        login.login(
            ReadConfig.get_username(),
            ReadConfig.get_password()
        )
        assert "inventory" in driver.current_url
