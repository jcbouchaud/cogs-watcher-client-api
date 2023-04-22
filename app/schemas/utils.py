from pydantic import BaseModel
from humps import camelize


def to_camel(string: str):
    return camelize(string)


class CamelBaseModel(BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True