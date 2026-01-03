from sqlalchemy.orm import Session
from .models import Note, Tag

def create_note(db: Session, title: str, content: str, tags: list):
    note = Note(title=title, content=content)
    for tag_name in tags:
        tag = db.query(Tag).filter(Tag.name == tag_name).first()
        if not tag:
            tag = Tag(name=tag_name)
        note.tags.append(tag)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note
