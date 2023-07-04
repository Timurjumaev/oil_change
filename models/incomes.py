from db import Base
from sqlalchemy import *


class Incomes(Base):
    __tablename__ = "incomes"
    id = Column(Integer, autoincrement=True, primary_key=True)
    order_id = Column(Integer)
    money = Column(Numeric)
    date = Column(DateTime)
    comment = Column(String(999))
    branch_id = Column(Integer)
