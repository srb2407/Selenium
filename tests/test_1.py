import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestLogin:
    def testLoginUsers(self):
        user = self.driver.find_element(By.ID, 'user-name')
        user.clear()
        user.send_keys("standard_user")
        passw = self.driver.find_element(By.ID, 'password')
        passw.clear()
        passw.send_keys("secret_sauce")
        self.driver.find_element(By.ID, 'login-button').click()
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        wait = WebDriverWait(self.driver, 10)
        logout = wait.until(EC.element_to_be_clickable(self.driver.find_element(By.ID, "logout_sidebar_link")))
        logout.click()
        self.driver.quit()
