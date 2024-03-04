from allure import step
from data.consts import API_BASE_URL
import requests
from models.create import EntityRequestModel
from models.get_all import GetAllResponseModel, EntityItem


class ApiClient:
    @step
    def request(self, method, short_url, json=None) -> requests.Response:
        match method.lower():
            case "post":
                req = requests.post
            case "get":
                req = requests.get
            case "delete":
                req = requests.delete
            case "patch":
                req = requests.patch
        response = req(url=f"{API_BASE_URL}{short_url}", json=json)
        with step(f"Response: {response.text}"):
            pass
        return response

    def create(self, entity_request: EntityRequestModel = None) -> str:
        if entity_request:
            model = entity_request.model_dump()
        else:
            model = EntityRequestModel().model_dump()
        response = self.request("post", "/api/create", json=model)
        return response.text

    def delete(self, id_):
        response = self.request("delete", f"/api/delete/{id_}")
        return response.text

    def get_all(self) -> list[EntityItem]:
        response = self.request("get", "/api/getAll")
        return GetAllResponseModel.model_validate_json(response.text).entity

    def get(self, id_) -> EntityItem:
        response = self.request("get", f"/api/get/{id_}")
        return EntityItem.model_validate_json(response.text)

    def patch(self, id_, entity_request: EntityRequestModel = None):
        if entity_request:
            model = entity_request.model_dump()
        else:
            model = EntityRequestModel().model_dump()
        response = self.request("patch", f"/api/patch/{id_}", json=model)
        return response

    def clear_all_entities(self):
        for e in self.get_all():
            self.delete(e.id)

    def create_filler_entities(self):
        self.create()
        self.create()

    def create_test_entity(self, entity_before: EntityRequestModel):
        with step("Создаем тестовую сущность"):
            created_id = self.create(entity_request=entity_before)
        return created_id

    def get_entity_request_model(self, json_dict) -> EntityRequestModel:
        return EntityRequestModel.model_validate(json_dict)
