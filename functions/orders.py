from datetime import date
from sqlalchemy.orm import joinedload
from models.customers import Customers
from models.incomes import Incomes
from models.orders import Orders
from models.trades import Trades
from utils.db_operations import save_in_db, get_in_db
from fastapi import HTTPException
from utils.pagination import pagination


def all_orders(customer_id, ident, search, page, limit, db, user):
    if page < 0 or limit < 0:
        raise HTTPException(status_code=400, detail="page yoki limit 0 dan kichik kiritilmasligi kerak!")
    orders = db.query(Orders).\
        filter(Orders.branch_id == user.branch_id).\
        options(joinedload(Orders.customer),
                joinedload(Orders.trades))
    if customer_id:
        customer_filter = Orders.customer_id == customer_id
    else:
        customer_filter = Orders.id > 0
    if ident:
        ident_filter = Orders.id == ident
    else:
        ident_filter = Orders.id > 0
    if search:
        search_format = "%{}%".format(search)
        search_filter = (Customers.name.like(search_format)) | \
                        (Customers.number.like(search_format))
    else:
        search_filter = Orders.id > 0
    orders = orders.filter(customer_filter, ident_filter, search_filter).order_by(Orders.id.desc())
    return pagination(orders, page, limit)


def create_order_r(customer_id, db, user):
    get_in_db(db, Customers, customer_id, user)
    new = Orders(
        customer_id=customer_id,
        status=False,
        date=date.today(),
        branch_id=user.branch_id
    )
    save_in_db(db, new)


def update_order_r(ident, db, user):
    get_in_db(db, Orders, ident, user)
    if db.query(Trades).filter(Trades.order_id == ident).first() is None:
        raise HTTPException(status_code=400, detail="Buyurtmani faollashtirish uchun eng "
                                                    "kamida bitta savdo qo'shishingiz kerak")
    db.query(Orders).filter(Orders.id == ident).update({
        Orders.status: True
    })
    db.commit()
    money = 0
    trades = db.query(Trades).filter(Trades.order_id == ident).all()
    for trade in trades:
        money += (trade.amount * trade.price)
    new = Incomes(
        order_id=ident,
        money=money,
        date=date.today(),
        branch_id=user.branch_id
    )
    save_in_db(db, new)


def delete_order_r(ident, db, user):
    if get_in_db(db, Orders, ident, user).status:
        raise HTTPException(status_code=400, detail="Buyurtma allaqachon faollashgan!")
    db.query(Orders).filter(Orders.id == ident).delete()
    db.commit()

