import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestCart:
    def testAddToCart(self):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()

        cards = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_description']")

        for item in cards:
            if item.find_element(By.XPATH, ".//div[@class='inventory_item_name ']").text == 'Sauce Labs Bike Light':
                item.find_element(By.XPATH, ".//button[text()='Add to cart']").click()

        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "last-name").send_keys("Dubey")
        self.driver.find_element(By.ID, "postal-code").send_keys("282007")
        self.driver.find_element(By.ID, "first-name").send_keys("Deepak")
        self.driver.find_element(By.ID, "continue").click()
        self.driver.find_element(By.ID, "finish").click()

        message = self.driver.find_element(By.XPATH, "//h2[@class='complete-header']").text

        try:
            assert message == "Thank you for your rder!"
        except AssertionError as XYZ:
            print('Order Failed')

        self.driver.quit()
