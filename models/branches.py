from db import Base
from sqlalchemy import *


class Branches(Base):
    __tablename__ = "branches"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(999))
    status = Column(Boolean)

