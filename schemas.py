from pydantic import BaseModel
from datetime import date, time
from typing import Optional


class MeetingBase(BaseModel):
    title: str
    description: Optional[str] = None
    date: date
    time: time

class MeetingCreate(MeetingBase):
    pass

class Meeting(MeetingBase):
    id: int

    class Config:
        orm_mode = True
