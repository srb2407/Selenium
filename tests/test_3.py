from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestCart:
    def testAddToCart(self):
        ser_obj = Service()
        driver_options = Options()
        driver_options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(service=ser_obj, options=driver_options)
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()

        cards = driver.find_elements(By.XPATH, "//div[@class='inventory_item_description']")

        for item in cards:
            if item.find_element(By.XPATH, ".//div[@class='inventory_item_name ']").text == 'Sauce Labs Bike Light':
                item.find_element(By.XPATH, ".//button[text()='Add to cart']").click()

        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "last-name").send_keys("Dubey")
        driver.find_element(By.ID, "postal-code").send_keys("282007")
        driver.find_element(By.ID, "first-name").send_keys("Deepak")
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "finish").click()

        message = driver.find_element(By.XPATH, "//h2[@class='complete-header']").text

        try:
            assert message == "Thank you for your rder!"
        except AssertionError as XYZ:
            print('Order Failed')

