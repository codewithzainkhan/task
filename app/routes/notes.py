from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..schemas import NoteCreate, NoteResponse
from ..crud import create_note

router = APIRouter(prefix="/notes", tags=["Notes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=NoteResponse)
def add_note(note: NoteCreate, db: Session = Depends(get_db)):
    return create_note(db, note.title, note.content, note.tags)
