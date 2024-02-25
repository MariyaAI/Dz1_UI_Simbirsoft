from allure import step

from selenium.webdriver.chrome.webdriver import WebDriver
from pageobjects.page_actions import PageActions

TIMEOUT = 10


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver
        self._actions = PageActions(driver)

    def add_result_to_allure(self, result):
        with step(f"result: {result}"):
            pass
        return result
