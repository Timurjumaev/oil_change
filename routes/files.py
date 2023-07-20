from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session
from functions.files import create_file_e
from utils.login import get_current_active_user
from schemas.users import CreateUser
from db import database


files_router = APIRouter(
    prefix="/files",
    tags=["Files operation"]
)


@files_router.post("/create")
def create_file(product_id: int, new_file: UploadFile = File(None),
                db: Session = Depends(database), current_user: CreateUser = Depends(get_current_active_user)):
    create_file_e(product_id, new_file, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
