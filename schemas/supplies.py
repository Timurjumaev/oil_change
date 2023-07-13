from pydantic import BaseModel


class CreateSupply(BaseModel):
    name: str
    price: float
    amount: float
    amount_type: str
    category: str


class UpdateSupply(BaseModel):
    id: int
    name: str
    price: float
    amount: float
    amount_type: str
    category: str
    status: bool
