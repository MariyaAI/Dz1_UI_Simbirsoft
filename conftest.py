import pytest
from selenium import webdriver
from pageobjects.provider import PobjectProvider
from selenium.webdriver.chrome.service import Service
from api.client import ApiClient
from models.create import EntityRequestModel


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
    client.create_filler_entities()
    return client


@pytest.fixture
def entity_before(api_client: ApiClient):
    entity_before_dict = {
        "addition": {
            "additional_info": "test_api_create",
            "additional_number": 1234
        },
        "important_numbers": [
            1234,
            1234,
            1234
        ],
        "title": "Заголовок test_api_create",
        "verified": True
    }
    return api_client.get_entity_request_model(entity_before_dict)


@pytest.fixture
def test_entity_id(api_client: ApiClient, entity_before: EntityRequestModel):
    return api_client.create_test_entity(entity_before)
