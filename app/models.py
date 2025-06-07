from sqlalchemy import Column, Integer, String, Date, Time
from database import Base
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
