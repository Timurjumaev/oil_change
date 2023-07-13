from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import *
from models.customers import Customers


class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, autoincrement=True, primary_key=True)
    customer_id = Column(Integer)
    status = Column(Boolean)
    date = Column(Date)
    branch_id = Column(Integer)

    customer = relationship('Customers', foreign_keys=[customer_id],
                            primaryjoin=lambda: and_(Customers.id == Orders.customer_id))


