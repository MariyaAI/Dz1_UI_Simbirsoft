from pydantic import BaseModel


class Addition(BaseModel):
    additional_info: str = "Дополнительные сведения"
    additional_number: int = 321


class EntityRequestModel(BaseModel):
    addition: Addition = Addition()
    important_numbers: list[int] = [0, 1, 3]
    title: str = "Заголовок сущности"
    verified: bool = True
