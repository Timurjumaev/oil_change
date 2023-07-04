from db import Base
from sqlalchemy import *


class Trades(Base):
    __tablename__ = "trades"
    id = Column(Integer, autoincrement=True, primary_key=True)
    product_id = Column(Integer)
    amount = Column(Integer)
    order_id = Column(Integer)
    branch_id = Column(Integer)
