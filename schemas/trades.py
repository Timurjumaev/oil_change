from pydantic import BaseModel


class CreateTrade(BaseModel):
    product_id: int
    amount: float
    price: float
    order_id: int


class UpdateTrade(BaseModel):
    id: int
    product_id: int
    amount: float
    price: float
