import pytest
import allure
from allure import step
from api.client import ApiClient
from models.create import EntityRequestModel


@allure.suite("API тест 'Получение всех сущностей'")
@allure.title("API тест 'Получение всех сущностей'")
@pytest.mark.api
def test_api_get_all(api_client: ApiClient, test_entity_id: str, entity_before: EntityRequestModel):
    with step("1) Запрашиваем тестовую сущность по ID"):
        response_list = api_client.get_all()
        entity_after = response_list[-1]

    with step("2) Проверяем, что сущностей стало 3"):
        assert len(response_list) == 3

    with step("3) Проверяем поля До и После"):
        assert entity_after.addition.id == int(test_entity_id)
        assert entity_before.addition.additional_info == entity_after.addition.additional_info
        assert entity_before.addition.additional_number == entity_after.addition.additional_number
        assert entity_before.important_numbers == entity_after.important_numbers
        assert entity_before.title == entity_after.title
        assert entity_before.verified == entity_after.verified
