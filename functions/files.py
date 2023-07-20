import os
from fastapi import HTTPException
from models.files import Files
from models.products import Products
from utils.db_operations import save_in_db, get_in_db


def create_file_e(product_id, file, db, user):
    get_in_db(db, Products, product_id, user)
    file_location = file.filename
    ext = os.path.splitext(file_location)[-1].lower()
    if ext not in [".jpg", ".png", ".mp3", ".mp4", ".gif", ".jpeg"]:
        raise HTTPException(status_code=400, detail="Yuklanayotgan fayl formati mos kelmaydi!")
    with open(f"files/{file_location}", "wb+") as file_object:
        file_object.write(file.file.read())
    new_file_db = Files(
        file=file.filename,
        product_id=product_id,
        branch_id=user.branch_id
    )
    save_in_db(db, new_file_db)
