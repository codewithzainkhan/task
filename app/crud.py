from sqlalchemy.orm import Session
from sqlalchemy import or_
from .models import Note, Tag

def get_or_create_tag(db: Session, name: str):
    tag = db.query(Tag).filter(Tag.name == name).first()
    if not tag:
        tag = Tag(name=name)
        db.add(tag)
        db.commit()
        db.refresh(tag)
    return tag

def create_note(db: Session, title: str, content: str, tags: list):
    note = Note(title=title, content=content)
    for tag_name in tags:
        tag = get_or_create_tag(db, tag_name)
        note.tags.append(tag)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

def get_notes(db: Session):
    return db.query(Note).all()

def get_note_by_id(db: Session, note_id: int):
    return db.query(Note).filter(Note.id == note_id).first()

def update_note(db: Session, note: Note, title: str, content: str, tags: list):
    note.title = title
    note.content = content
    note.tags.clear()
    for tag_name in tags:
        tag = get_or_create_tag(db, tag_name)
        note.tags.append(tag)
    db.commit()
    db.refresh(note)
    return note

def delete_note(db: Session, note: Note):
    db.delete(note)
    db.commit()
