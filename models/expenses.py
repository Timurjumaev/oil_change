from db import Base
from sqlalchemy import *


class Expenses(Base):
    __tablename__ = "expenses"
    id = Column(Integer, autoincrement=True, primary_key=True)
    supply_id = Column(Integer)
    money = Column(Numeric)
    date = Column(DateTime)
    comment = Column(String(999), default="")
    branch_id = Column(Integer)
