from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.trades import all_trades, create_trade_e, update_trade_e, delete_trade_e
from schemas.trades import CreateTrade, UpdateTrade
from schemas.users import CreateUser
from utils.login import get_current_active_user
from db import database

trades_router = APIRouter(
    prefix="/trades",
    tags=["Trades operation"]
)


@trades_router.get("/get")
def get_trades(ident: int = None, order_id: int = None, db: Session = Depends(database), current_user:
               CreateUser = Depends(get_current_active_user)):
    return all_trades(ident, order_id, db, current_user)


@trades_router.post("/post")
def create_trade(new: CreateTrade, current_user: CreateUser = Depends(get_current_active_user),
                 db: Session = Depends(database)):
    create_trade_e(new, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@trades_router.put("/put")
def update_trade(this: UpdateTrade, db: Session = Depends(database),
                 current_user: CreateUser = Depends(get_current_active_user)):
    update_trade_e(UpdateTrade, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@trades_router.delete("/delete")
def delete_trade(ident: int, db: Session = Depends(database),
                 current_user: CreateUser = Depends(get_current_active_user)):
    delete_trade_e(ident, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
