from datetime import date
from models.expenses import Expenses
from models.products import Products
from utils.db_operations import save_in_db, get_in_db
from models.supplies import Supplies
from fastapi import HTTPException


def create_supply_y(form, db, user):
    if form.price <= 0 or form.amount <= 0:
        raise HTTPException(status_code=400, detail="Narx yoki miqdorda xatolik!")
    new = Supplies(
        name=form.name,
        price=form.price,
        amount=form.amount,
        amount_type=form.amount_type,
        category=form.category,
        date=date.today(),
        status=False,
        branch_id=user.branch_id
    )
    save_in_db(db, new)
    return new


def update_supply_y(form, db, user):
    if get_in_db(db, Supplies, form.id, user).status:
        raise HTTPException(status_code=400, detail="Tanlangan ta'minot allaqachon omborga qo'shilgan!")
    if form.price <= 0 or form.amount <= 0:
        raise HTTPException(status_code=400, detail="Narx yoki miqdorda xatolik!")
    if not form.status:
        db.query(Supplies).filter(Supplies.id == form.id).update({
            Supplies.name: form.name,
            Supplies.price: form.price,
            Supplies.amount: form.amount,
            Supplies.amount_type: form.amount_type,
            Supplies.category: form.category,
            Supplies.date: date.today(),
        })
        db.commit()
    else:
        db.query(Supplies).filter(Supplies.id == form.id).update({
            Supplies.name: form.name,
            Supplies.price: form.price,
            Supplies.amount: form.amount,
            Supplies.amount_type: form.amount_type,
            Supplies.category: form.category,
            Supplies.date: date.today(),
            Supplies.status: True
        })
        db.commit()
        new_supply = db.query(Supplies).filter(Supplies.id == form.id).first()
        product = db.query(Products).filter(Products.amount_type == form.amount_type,
                                            Products.category == form.category,
                                            Products.name == form.name,
                                            Products.price == form.price)
        new_expense = Expenses(
            supply_id=form.id,
            money=new_supply.amount * new_supply.price,
            date=date.today(),
            branch_id=user.branch_id
        )
        save_in_db(db, new_expense)
        if product.first():
            product.update({
                Products.amount: Products.amount + form.amount,
                Products.date: date.today()
            })
            db.commit()
        else:
            new = Products(
                name=form.name,
                price=form.price,
                amount=form.amount,
                amount_type=form.amount_type,
                category=form.category,
                date=date.today(),
                branch_id=user.branch_id
            )
            save_in_db(db, new)
            return new
        return "Amaliyot muvofaqqiyatli yakunlandi!"


def delete_supply_y(ident, db, user):
    supply = get_in_db(db, Supplies, ident, user)
    if supply.status:
        raise HTTPException(status_code=400, detail="Tanlangan ta'minot allaqachon omborga qo'shilgan!")
    else:
        db.query(Supplies).filter(Supplies.id == supply.id).delete()
        db.commit()

