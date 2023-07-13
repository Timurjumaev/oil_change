from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.customers import all_customers, create_customer_r, update_customer_r, delete_customer_r
from schemas.users import CreateUser
from utils.login import get_current_active_user
from schemas.customers import CreateCustomer, UpdateCustomer
from db import database

customers_router = APIRouter(
    prefix="/customers",
    tags=["Customers operation"]
)


@customers_router.get("/get")
def get_customers(ident: int = None, search: str = None, page: int = 0, limit: int = 25,
                  db: Session = Depends(database), current_user: CreateUser = Depends(get_current_active_user)):
    return all_customers(ident, search, page, limit, db, current_user)


@customers_router.post("/post")
def create_customer(new: CreateCustomer, current_user: CreateUser = Depends(get_current_active_user),
                    db: Session = Depends(database)):
    create_customer_r(new, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@customers_router.put("/put")
def update_customer(this: UpdateCustomer, db: Session = Depends(database),
                    current_user: CreateUser = Depends(get_current_active_user)):
    update_customer_r(this, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@customers_router.delete("/delete")
def delete_customer(ident: int, db: Session = Depends(database),
                    current_user: CreateUser = Depends(get_current_active_user)):
    delete_customer_r(ident, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
