from db import Base
from sqlalchemy import *


class Supplies(Base):
    __tablename__ = "supplies"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(999))
    price = Column(Numeric)
    amount = Column(Integer)
    amount_type = Column(String(999))
    category = Column(String(999))
    date = Column(Date)
    status = Column(Boolean)
    branch_id = Column(Integer)
