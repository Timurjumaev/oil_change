from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from db import Base


def get_in_db(
        db: Session,
        model,
        ident: int,
        user
):
    obj = db.query(model).filter(model.id == ident, model.branch_id == user.branch_id).first()
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Bazada bunday {model} yo'q"
        )
    return obj


def save_in_db(
        db: Session,
        obj: Base
):
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
