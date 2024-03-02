from random import randint
import pytest
import allure
from allure import step
from api.client import ApiClient


@allure.suite("API тест 'Создание сущности'")
@allure.title("API тест 'Создание сущности'")
@pytest.mark.api
def test_api_create(api_client: ApiClient):
    with step("1) Создаем тестовую сущность"):
        entity_before_dict = {
            "addition": {
                "additional_info": "test_api_create",
                "additional_number": randint(0, 1234)
            },
            "important_numbers": [
                randint(0, 1234),
                randint(0, 1234),
                randint(0, 1234)
            ],
            "title": "Заголовок test_api_create",
            "verified": True
        }
        entity_before = api_client.get_entity_request_model(entity_before_dict)
        created_id = api_client.create(entity_request=entity_before)

    with step("2) Запрашиваем тестовую сущность по ID"):
        entity_after = api_client.get(created_id)

    with step("3) Проверяем поля До и После"):
        assert entity_before.addition.additional_info == entity_after.addition.additional_info
        assert entity_before.addition.additional_number == entity_after.addition.additional_number
        assert entity_before.important_numbers == entity_after.important_numbers
        assert entity_before.title == entity_after.title
        assert entity_before.verified == entity_after.verified
