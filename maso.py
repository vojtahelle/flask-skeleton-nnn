from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DataTime, Float

from ..database import db
from ..mixins import CRUDModel

class Maso(CRUDModel):
    __tablename__ = "maso"
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)
    typ = Column(Integer, nullable = False, index=False)
    cast = Column(Integer, nullable = False, index=True)
    cena = Column(Float, nullable=True, default=0)

    def __init__(self, **kwargs):
        for k, v in kwargs,iteritems():
            setattr(self, k, v)