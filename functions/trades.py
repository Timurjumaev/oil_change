from models.orders import Orders
from models.products import Products
from models.trades import Trades
from utils.db_operations import save_in_db, get_in_db
from fastapi import HTTPException


def all_trades(ident, order_id, db, user):
    trades = db.query(Trades).filter(Trades.branch_id == user.branch_id)
    if ident:
        ident_filter = Trades.id == ident
    else:
        ident_filter = Trades.id > 0
    if order_id:
        order_id_filter = Trades.order_id == order_id
    else:
        order_id_filter = Trades.id > 0
    return trades.filter(ident_filter, order_id_filter).order_by(Trades.id.desc()).all()


def create_trade_e(form, db, user):
    get_in_db(db, Products, form.product_id, user), get_in_db(db, Orders, form.order_id, user)
    order = db.query(Orders).filter(Orders.id == form.order_id).first()
    if order.status:
        raise HTTPException(status_code=400, detail="Kechirasiz, ushbu buyurtma allaqachon sotilgan!")
    product = db.query(Products).filter(Products.id == form.product_id).first()
    if product.amount < form.amount:
        raise HTTPException(status_code=400, detail=f"Kechirasiz, omborda {product.name} yetarli emas!")
    if form.price < 0:
        raise HTTPException(status_code=400, detail="Narx manfiy bo'lishi mumkin emas!")
    new = Trades(
        product_id=form.product_id,
        amount=form.amount,
        price=form.price,
        order_id=form.order_id,
        branch_id=user.branch_id
    )
    save_in_db(db, new)
    db.query(Products).filter(Products.id == form.product_id).update({
        Products.amount: Products.amount - form.amount
    })
    db.commit()


def update_trade_e(form, db, user):
    get_in_db(db, Trades, form.id, user), get_in_db(db, Products, form.product_id, user), \
        get_in_db(db, Orders, form.order_id, user)
    trade = get_in_db(db, Trades, form.id, user)
    order = db.query(Orders).filter(Orders.id == trade.order_id).first()
    if order.status:
        raise HTTPException(status_code=400, detail="Kechirasiz, ushbu savdo tegishli bo'lgan "
                                                    "buyurtma allaqachon sotilgan!")
    product = db.query(Products).filter(Products.id == form.product_id).first()
    if product.amount < form.amount:
        raise HTTPException(status_code=400, detail=f"Kechirasiz, omborda {product.name} yetarli emas!")
    if form.price < 0:
        raise HTTPException(status_code=400, detail="Narx manfiy bo'lishi mumkin emas!")
    old_trade = db.query(Trades).filter(Trades.id == form.id).first()
    db.query(Trades).filter(Trades.id == form.id).update({
        Trades.product_id: form.product_id,
        Trades.amount: form.amount,
        Trades.price: form.price
    })
    db.commit()
    new_trade = db.query(Trades).filter(Trades.id == form.id).first()
    if old_trade.product_id == new_trade.product_id:
        db.query(Products).filter(Products.id == form.product_id).update({
            Products.amount: Products.amount + old_trade.amount - new_trade.amount
        })
        db.commit()
    else:
        db.query(Products).filter(Products.id == new_trade.product_id).update({
            Products.amount: Products.amount - new_trade.amount
        })
        db.query(Products).filter(Products.id == old_trade.product_id).update({
            Products.amount: Products.amount + old_trade.amount
        })
        db.commit()


def delete_trade_e(ident, db, user):
    trade = get_in_db(db, Trades, ident, user)
    if get_in_db(db, Orders, trade.order_id, user).status:
        raise HTTPException(status_code=400, detail="Kechirasiz, ushbu savdo tegishli bo'lgan "
                                                    "buyurtma allaqachon sotilgan!")
    trade = db.query(Trades).filter(Trades.id == ident).first()
    db.query(Trades).filter(Trades.id == ident).delete()
    db.query(Products).filter(Products.id == trade.product_id).update({
        Products.amount: Products.amount + trade.amount
    })
    db.commit()



