from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.customers import Customers
from models.expenses import Expenses
from models.incomes import Incomes
from models.products import Products
from schemas.users import CreateUser
from utils.login import get_current_active_user
from db import database

statistics_router = APIRouter(
    prefix="/statistics",
    tags=["Statistics operation"]
)


@statistics_router.get("/expenses")
def get_expenses(start: date = date.today(), end: date = date.today(), current_user:
                 CreateUser = Depends(get_current_active_user), db: Session = Depends(database)):
    expenses = db.query(Expenses).filter(Expenses.branch_id == current_user.branch_id,
                                         Expenses.date <= end, Expenses.date >= start).all()
    money = 0
    for expense in expenses:
        money += expense.money
    return money


@statistics_router.get("/incomes")
def get_incomes(start: date = date.today(), end: date = date.today(), current_user:
                CreateUser = Depends(get_current_active_user), db: Session = Depends(database)):
    incomes = db.query(Incomes).filter(Incomes.branch_id == current_user.branch_id,
                                       Incomes.date <= end, Incomes.date >= start).all()
    money = 0
    for income in incomes:
        money += income.money
    return money


@statistics_router.get("/profit")
def get_profit(start: date = date.today(), end: date = date.today(), current_user:
               CreateUser = Depends(get_current_active_user), db: Session = Depends(database)):
    expense = get_expenses(start, end, current_user, db)
    income = get_incomes(start, end, current_user, db)
    profit = income - expense
    return profit


@statistics_router.get("/total_products")
def get_total_products(current_user: CreateUser = Depends(get_current_active_user), db: Session = Depends(database)):
    products = db.query(Products).filter(Products.branch_id == current_user.branch_id).all()
    money = 0
    for product in products:
        money += product.price * product.amount
    return money


@statistics_router.get("/total_customers")
def get_total_customers(start: date = date.today(), end: date = date.today(), current_user:
                        CreateUser = Depends(get_current_active_user), db: Session = Depends(database)):
    customers = db.query(Customers).filter(Customers.branch_id == current_user.branch_id,
                                           Customers.date <= end, Customers.date >= start).all()

    return len(customers)








