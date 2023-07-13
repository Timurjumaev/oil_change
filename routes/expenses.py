from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.expenses import all_expenses, create_expense_e
from schemas.users import CreateUser
from utils.login import get_current_active_user
from schemas.expenses import CreateExpense
from db import database

expenses_router = APIRouter(
    prefix="/expenses",
    tags=["Expenses operation"]
)


@expenses_router.get("/get")
def get_expenses(ident: int = None, search: str = None, page: int = 0, limit: int = 25,
                 db: Session = Depends(database), current_user: CreateUser = Depends(get_current_active_user)):
    return all_expenses(ident, search, page, limit, db, current_user)


@expenses_router.post("/post")
def create_expense(new: CreateExpense, current_user: CreateUser = Depends(get_current_active_user),
                   db: Session = Depends(database)):
    create_expense_e(new, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
