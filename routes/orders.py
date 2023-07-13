from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.orders import all_orders, create_order_r, update_order_r, delete_order_r
from schemas.users import CreateUser
from utils.login import get_current_active_user
from db import database

orders_router = APIRouter(
    prefix="/orders",
    tags=["Orders operation"]
)


@orders_router.get("/get")
def get_orders(ident: int = None, search: str = None, page: int = 0, limit: int = 25,
               db: Session = Depends(database), current_user: CreateUser = Depends(get_current_active_user)):
    return all_orders(ident, search, page, limit, db, current_user)


@orders_router.post("/post")
def create_order(customer_id: int, current_user: CreateUser = Depends(get_current_active_user),
                 db: Session = Depends(database)):
    create_order_r(customer_id, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@orders_router.put("/put")
def update_order(ident: int, db: Session = Depends(database),
                 current_user: CreateUser = Depends(get_current_active_user)):
    update_order_r(ident, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@orders_router.delete("/delete")
def delete_order(ident: int, db: Session = Depends(database),
                 current_user: CreateUser = Depends(get_current_active_user)):
    delete_order_r(ident, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
