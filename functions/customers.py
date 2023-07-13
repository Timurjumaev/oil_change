from datetime import date
from models.customers import Customers
from models.orders import Orders
from utils.db_operations import save_in_db, get_in_db
from fastapi import HTTPException
from utils.pagination import pagination


def all_customers(ident, search, page, limit, db, user):
    if page < 0 or limit < 0:
        raise HTTPException(status_code=400, detail="page yoki limit 0 dan kichik kiritilmasligi kerak!")
    customers = db.query(Customers).filter(Customers.branch_id == user.branch_id)
    if ident:
        ident_filter = Customers.id == ident
    else:
        ident_filter = Customers.id > 0
    if search:
        search_format = "%{}%".format(search)
        search_filter = (Customers.name.like(search_format)) | \
                        (Customers.number.like(search_format))
    else:
        search_filter = Customers.id > 0
    customers = customers.filter(ident_filter, search_filter).order_by(Customers.id.desc())
    return pagination(customers, page, limit)


def create_customer_r(form, db, user):
    if db.query(Customers).filter(Customers.number == form.number).first():
        raise HTTPException(status_code=400, detail="Bunday avtoraqamli mijoz allaqachon ro'yxatdan o'tgan!")
    new = Customers(
        name=form.name,
        number=form.number,
        date=date.today(),
        branch_id=user.branch_id
    )
    save_in_db(db, new)


def update_customer_r(form, db, user):
    customer = get_in_db(db, Customers, form.id, user)
    if db.query(Customers).filter(Customers.number == form.number).first() and customer.number != form.number:
        raise HTTPException(status_code=400, detail="Bunday avtoraqamli mijoz allaqachon ro'yxatdan o'tgan!")
    if db.query(Orders).filter(Orders.customer_id == form.id).first():
        raise HTTPException(status_code=400, detail="Bu mijozga allaqachon buyurtma qo'shilgan!")
    db.query(Customers).filter(Customers.id == form.id).update({
        Customers.name: form.name,
        Customers.number: form.number,
        Customers.date: date.today(),
    })
    db.commit()


def delete_customer_r(ident, db, user):
    get_in_db(db, Customers, ident, user)
    if db.query(Orders).filter(Orders.customer_id == ident).first():
        raise HTTPException(status_code=400, detail="Bu mijozga allaqachon buyurtma qo'shilgan!")
    db.query(Customers).filter(Customers.id == ident).delete()
    db.commit()

