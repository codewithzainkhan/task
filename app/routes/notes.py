from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas
from ..deps import get_db, get_current_user

router = APIRouter(prefix="/notes", tags=["Notes"])


@router.post("/", response_model=schemas.NoteResponse)
def create_note(
    note: schemas.NoteCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    tags = []
    for name in note.tags:
        tag = db.query(models.Tag).filter_by(name=name).first()
        if not tag:
            tag = models.Tag(name=name)
        tags.append(tag)

    new_note = models.Note(
        title=note.title,
        content=note.content,
        owner=user,
        tags=tags,
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


@router.get("/", response_model=List[schemas.NoteResponse])
def list_notes(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return db.query(models.Note).filter_by(user_id=user.id).all()


@router.delete("/{note_id}")
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    note = db.query(models.Note).filter_by(id=note_id, user_id=user.id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    db.delete(note)
    db.commit()
    return {"message": "Note deleted"}
