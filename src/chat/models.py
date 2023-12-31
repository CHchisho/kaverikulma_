from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean, MetaData
from datetime import datetime

from database import Base


class Messages(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    id_sender = Column(Integer)
    id_recipient = Column(Integer)
    # send_at = Column(String, default=now.strftime("%m.%d.%Y, %H:%M:%S"))
    send_at = Column(String)
    message = Column(String)

    # def new_date(self):
    #     global now
    #     now = datetime.now()
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Match(Base):
    __tablename__ = "match"


    id = Column(Integer, primary_key=True)
    id_sender = Column(Integer)
    id_recipient = Column(Integer)
    answer = Column(Integer) # 0-None  1-True  2-False

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}