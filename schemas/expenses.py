from pydantic import BaseModel


class CreateExpense(BaseModel):
    money: float
    comment: str
