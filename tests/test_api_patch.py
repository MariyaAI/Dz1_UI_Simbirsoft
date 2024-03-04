import pytest
import allure
from allure import step
from api.client import ApiClient
from models.create import EntityRequestModel


@allure.suite("API тест 'Изменение сущности'")
@allure.title("API тест 'Изменение сущности'")
@pytest.mark.api
def test_api_patch(api_client: ApiClient, test_entity_id: str, entity_before: EntityRequestModel):
    with step("1) Изменяем тестовую сущность по ID"):
        entity_after_dict = {
            "addition": {
                "additional_info": "test_api_patch_after",
                "additional_number": 2345
            },
            "important_numbers": [
                2345,
                2345,
                2345
            ],
            "title": "Заголовок test_api_patch_after",
            "verified": True
        }
        entity_after_request = api_client.get_entity_request_model(entity_after_dict)
        api_client.patch(test_entity_id, entity_request=entity_after_request)
        entity_after = api_client.get(test_entity_id)

    with step("2) Проверяем поля До и После"):
        assert entity_after.addition.id == int(test_entity_id)
        assert entity_before.addition.additional_info != entity_after.addition.additional_info
        assert entity_before.addition.additional_number != entity_after.addition.additional_number
        assert entity_before.important_numbers != entity_after.important_numbers
        assert entity_before.title != entity_after.title
        assert entity_before.verified == entity_after.verified
