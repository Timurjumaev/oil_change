from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.users import users_router
from utils.login import login_router

app = FastAPI()

app.include_router(login_router)
app.include_router(users_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)
