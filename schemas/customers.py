from pydantic import BaseModel


class CreateCustomer(BaseModel):
    name: str
    number: str


class UpdateCustomer(BaseModel):
    id: int
    name: str
    number: str
