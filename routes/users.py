from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.users import create_user_r, update_user_r
from utils.login import get_current_active_user
from schemas.users import CreateUser, UpdateUser
from db import database

users_router = APIRouter(
    prefix="/users",
    tags=["Users operation"]
)


@users_router.get("/get")
def get_users(current_user: CreateUser = Depends(get_current_active_user)):
    return current_user


@users_router.post("/post")
def create_user(new_user: CreateUser, db: Session = Depends(database)):
    create_user_r(new_user, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@users_router.put("/put")
def update_user(this_user: UpdateUser, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    update_user_r(this_user, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
