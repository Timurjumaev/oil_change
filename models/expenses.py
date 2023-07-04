from db import Base
from sqlalchemy import *


class Expenses(Base):
    __tablename__ = "expenses"
    id = Column(Integer, autoincrement=True, primary_key=True)
    product_id = Column(Integer)
    amount = Column(Integer)
    money = Column(Numeric)
    date = Column(DateTime)
    comment = Column(String(999))
    branch_id = Column(Integer)
