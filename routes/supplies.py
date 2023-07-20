from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.supplies import create_supply_y, update_supply_y, delete_supply_y
from schemas.users import CreateUser
from utils.login import get_current_active_user
from schemas.supplies import CreateSupply, UpdateSupply
from db import database

supplies_router = APIRouter(
    prefix="/supplies",
    tags=["Supplies operation"]
)


@supplies_router.post("/post")
def create_supply(new: CreateSupply, current_user: CreateUser = Depends(get_current_active_user),
                  db: Session = Depends(database)):
    return create_supply_y(new, db, current_user)


@supplies_router.put("/put")
def update_supply(this: UpdateSupply, db: Session = Depends(database),
                  current_user: CreateUser = Depends(get_current_active_user)):
    return update_supply_y(this, db, current_user)


@supplies_router.delete("/delete")
def delete_supply(ident: int, db: Session = Depends(database),
                  current_user: CreateUser = Depends(get_current_active_user)):
    delete_supply_y(ident, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
