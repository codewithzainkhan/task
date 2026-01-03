from sqlalchemy import Column, Integer, String, Text, Table, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

note_tags = Table(
    "note_tags",
    Base.metadata,
    Column("note_id", ForeignKey("notes.id")),
    Column("tag_id", ForeignKey("tags.id")),
)

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    tags = relationship("Tag", secondary=note_tags)

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
