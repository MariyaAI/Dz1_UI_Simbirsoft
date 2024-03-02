from random import randint
import pytest
import allure
from allure import step
from api.client import ApiClient


@allure.suite("API тест 'Удаление сущности'")
@allure.title("API тест 'Удаление сущности'")
@pytest.mark.api
def test_api_delete(api_client: ApiClient):
    with step("1) Создаем тестовую сущность"):
        entity_before_dict = {
            "addition": {
                "additional_info": "test_api_delete",
                "additional_number": randint(0, 1234)
            },
            "important_numbers": [
                randint(0, 1234),
                randint(0, 1234),
                randint(0, 1234)
            ],
            "title": "Заголовок test_api_delete",
            "verified": True
        }
        entity_before = api_client.get_entity_request_model(entity_before_dict)
        created_id = api_client.create(entity_request=entity_before)

    with step("2) Удаляем тестовыую сущность"):
        api_client.delete(created_id)

    with step("3) Запрашиваем все сущности"):
        response_list = api_client.get_all()

    with step("4) Проверяем, что сущностей осталось 2"):
        assert len(response_list) == 2

    with step("5) Проверяем, что ID удаленной сущности нет в списке"):
        for e in response_list:
            assert created_id != str(e.addition.id)
