from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from ..database import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.Meeting])
def list_meetings(db: Session = Depends(get_db)):
    return crud.get_meetings(db)

@router.get("/{meeting_id}", response_model=schemas.Meeting)
def get_meeting(meeting_id: int, db: Session = Depends(get_db)):
    meeting = crud.get_meeting(db, meeting_id)
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    return meeting

@router.post("/", response_model=schemas.Meeting)
def create_meeting(meeting: schemas.MeetingCreate, db: Session = Depends(get_db)):
    return crud.create_meeting(db, meeting)

@router.put("/{meeting_id}", response_model=schemas.Meeting)
def update_meeting(meeting_id: int, meeting: schemas.MeetingCreate, db: Session = Depends(get_db)):
    return crud.update_meeting(db, meeting_id, meeting)

@router.delete("/{meeting_id}")
def delete_meeting(meeting_id: int, db: Session = Depends(get_db)):
    crud.delete_meeting(db, meeting_id)
    return {"message": "Meeting deleted"}
