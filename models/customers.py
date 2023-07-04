from db import Base
from sqlalchemy import *


class Customers(Base):
    __tablename__ = "customers"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(999))
    number = Column(String(999))
    date = Column(Date)
    branch_id = Column(Integer)

