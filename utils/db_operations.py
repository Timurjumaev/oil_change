from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from db import Base
from models.branches import Branches


def get_in_db(
        db: Session,
        model,
        ident: int,
        user
):
    obj = db.query(model).filter(model.id == ident, model.branch_id == user.branch_id).first()
    branch = db.query(Branches).filter(Branches.id == obj.branch_id).first()
    if not obj or not branch.status:
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
