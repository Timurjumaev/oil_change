from utils.db_operations import save_in_db
from models.users import Users
from utils.login import get_password_hash
from fastapi import HTTPException


def create_user_r(form, db):
    password_hash = get_password_hash(form.password)
    new_user_db = Users(
        username=form.username,
        password=form.password,
        password_hash=password_hash,
        branch_id=form.branch_id
    )
    save_in_db(db, new_user_db)


def update_user_r(form, db, user):
    if user.id != form.id:
        raise HTTPException(status_code=400, detail="Bunday foydalanuvchi mavjud emas!")
    password_hash = get_password_hash(form.password)
    db.query(Users).filter(Users.id == form.id).update({
        Users.username: form.username,
        Users.password: form.password,
        Users.password_hash: password_hash,
    })
    db.commit()





