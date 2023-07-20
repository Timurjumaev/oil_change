from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.users import users_router
from utils.login import login_router
from routes.supplies import supplies_router
from routes.products import products_router
from routes.customers import customers_router
from routes.orders import orders_router
from routes.trades import trades_router
from routes.expenses import expenses_router
from routes.statistics import statistics_router
from routes.files import files_router


app = FastAPI()

app.include_router(login_router)
app.include_router(users_router)
app.include_router(supplies_router)
app.include_router(products_router)
app.include_router(customers_router)
app.include_router(orders_router)
app.include_router(trades_router)
app.include_router(expenses_router)
app.include_router(statistics_router)
app.include_router(files_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)
