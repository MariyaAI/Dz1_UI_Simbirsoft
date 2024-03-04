import pytest
import allure
from allure import step
from api.client import ApiClient


@allure.suite("API тест 'Удаление сущности'")
@allure.title("API тест 'Удаление сущности'")
@pytest.mark.api
@pytest.mark.api
def test_api_delete(api_client: ApiClient, test_entity_id: str):
    with step("1) Удаляем тестовыую сущность"):
        api_client.delete(test_entity_id)

    with step("2) Запрашиваем все сущности"):
        response_list = api_client.get_all()

    with step("3) Проверяем, что сущностей осталось 2"):
        assert len(response_list) == 2

    with step("4) Проверяем, что ID удаленной сущности нет в списке"):
        for e in response_list:
            assert test_entity_id != str(e.addition.id)
