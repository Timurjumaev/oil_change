from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.products import Products
from schemas.users import CreateUser
from utils.login import get_current_active_user
from db import database

products_router = APIRouter(
    prefix="/products",
    tags=["Products operation"]
)


@products_router.get("/get")
def get_products(ident: int = None, search: str = None, category: str = None,
                 current_user: CreateUser = Depends(get_current_active_user), db: Session = Depends(database)):
    products = db.query(Products).filter(Products.branch_id == current_user.branch_id)
    if ident:
        ident_filter = Products.id == ident
    else:
        ident_filter = Products.id > 0
    if search:
        search_format = "%{}%".format(search)
        search_filter = (Products.name.like(search_format)) | \
                        (Products.price.like(search_format))
    else:
        search_filter = Products.id > 0
    if category:
        category_filter = Products.category == category
    else:
        category_filter = Products.id > 0
    return products.filter(search_filter, category_filter, ident_filter).order_by(Products.id.desc()).all()


