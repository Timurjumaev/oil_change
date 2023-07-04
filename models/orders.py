from db import Base
from sqlalchemy import *


class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, autoincrement=True, primary_key=True)
    customer_id = Column(Integer)
    status = Column(Boolean)
    date = Column(Date)
    branch_id = Column(Integer)
