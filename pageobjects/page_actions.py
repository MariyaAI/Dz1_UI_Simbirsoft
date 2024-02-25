import time
from allure import step
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

TIMEOUT = 10


class PageActions:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver

    @step
    def wait_for_seconds(self, seconds: int):
        time.sleep(seconds)

    @step
    def find_element(self, locator: tuple, timeout=TIMEOUT) -> WebElement:
        return WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @step
    def find_elements(self, locator: tuple, timeout=TIMEOUT) -> list[WebElement]:
        try:
            return WebDriverWait(self._driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except ValueError:
            return []

    @step
    def accept_alert(self):
        WebDriverWait(self._driver, TIMEOUT).until(EC.alert_is_present())
        self._driver.switch_to.alert.accept()

    @step
    def click(self, locator: tuple):
        self.find_element(locator).click()

    @step
    def send_keys(self, locator: tuple, text: str):
        self.find_element(locator).send_keys(text)

    @step
    def select_by_visible_text(self, locator: tuple, value: str):
        select = Select(self.find_element(locator))
        select.select_by_visible_text(value)
