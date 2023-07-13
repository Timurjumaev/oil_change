from sqlalchemy.orm import relationship

from db import Base
from sqlalchemy import *

from models.orders import Orders


class Trades(Base):
    __tablename__ = "trades"
    id = Column(Integer, autoincrement=True, primary_key=True)
    product_id = Column(Integer)
    amount = Column(Numeric)
    price = Column(Numeric)
    order_id = Column(Integer)
    branch_id = Column(Integer)

    order = relationship('Orders', foreign_keys=[order_id],
                         primaryjoin=lambda: and_(Orders.id == Trades.order_id), backref="trades")

