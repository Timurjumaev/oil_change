from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    password: str
    branch_id: int


class UpdateUser(BaseModel):
    id: int
    username: str
    password: str
