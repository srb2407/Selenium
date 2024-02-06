import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class TestSort:
    def testDataSorting(self):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()
        sort_options = Select((self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']")))
        sort_options.select_by_visible_text('Price (low to high)')

        driver = self.driver

        item_list = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")
        prices = []
        for i in item_list:
            price = i.text.split('$')[1]
            prices.append(float(price))
        sorted_list = sorted(prices)

        try:
            assert prices == sorted_list
        except AssertionError as SortError:
            print('Sort Failed')
        driver.quit()
