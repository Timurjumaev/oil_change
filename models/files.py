from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import *
from models.products import Products


class Files(Base):
    __tablename__ = "files"
    id = Column(Integer, autoincrement=True, primary_key=True)
    file = Column(String(999))
    product_id = Column(Integer)
    branch_id = Column(Integer)

    product = relationship('Products', foreign_keys=[product_id],
                           primaryjoin=lambda: and_(Products.id == Files.product_id), backref="file")
