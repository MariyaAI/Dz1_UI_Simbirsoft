from selenium.webdriver.chrome.webdriver import WebDriver
from pageobjects.page_actions import PageActions
from pageobjects.manager_page import ManagerPage
from pageobjects.customers_table import CustomersTable
from pageobjects.add_customer_form import AddCustomerForm


class PobjectProvider:
    def __init__(self, driver: WebDriver) -> None:
        self.page_actions = PageActions(driver)
        self.manager_page = ManagerPage(driver)
        self.customers_table = CustomersTable(driver)
        self.add_customer_form = AddCustomerForm(driver)
