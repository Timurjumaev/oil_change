from datetime import date
from utils.db_operations import save_in_db
from models.expenses import Expenses
from fastapi import HTTPException
from utils.pagination import pagination


def all_expenses(ident, search, page, limit, db, user):
    if page < 0 or limit < 0:
        raise HTTPException(status_code=400, detail="page yoki limit 0 dan kichik kiritilmasligi kerak!")
    expenses = db.query(Expenses).filter(Expenses.branch_id == user.branch_id, Expenses.supply_id == 0)
    if ident:
        ident_filter = Expenses.id == ident
    else:
        ident_filter = Expenses.id > 0
    if search:
        search_format = "%{}%".format(search)
        search_filter = (Expenses.comment.like(search_format))
    else:
        search_filter = Expenses.id > 0
    expenses = expenses.filter(ident_filter, search_filter).order_by(Expenses.id.desc())
    return pagination(expenses, page, limit)


def create_expense_e(form, db, user):
    new = Expenses(
        supply_id=0,
        money=form.money,
        date=date.today(),
        comment=form.comment,
        branch_id=user.branch_id
    )
    save_in_db(db, new)



