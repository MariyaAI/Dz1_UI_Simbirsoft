import pytest
from selenium import webdriver
from pageobjects.provider import PobjectProvider
from selenium.webdriver.chrome.service import Service
from api.client import ApiClient


@pytest.fixture
def driver():
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=600,980")
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(5)
    yield driver
    driver.quit()


@pytest.fixture
def provider(driver):
    return PobjectProvider(driver)


@pytest.fixture
def api_client():
    client = ApiClient()
    client.clear_all_entities()
    client.create_test_entities()
    return client
