from allure import step
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage
from data.consts import MANAGER_URL


class ManagerPage(BasePage):
    btn_add_cust = (By.XPATH, '//*[@ng-click="addCust()"]')
    btn_open_account = (By.XPATH, '//*[@ng-click="openAccount()"]')
    btn_show_cust = (By.XPATH, '//*[@ng-click="showCust()"]')
    tbody = (By.XPATH, '//tbody')

    @step
    def navigate(self):
        with step(f"goto: {MANAGER_URL}"):
            self._driver.get(MANAGER_URL)
