from typing import List

from pydantic import BaseModel


class Addition(BaseModel):
    id: int
    additional_info: str
    additional_number: int


class EntityItem(BaseModel):
    id: int
    title: str
    verified: bool
    addition: Addition
    important_numbers: List[int]


class GetAllResponseModel(BaseModel):
    entity: List[EntityItem]
