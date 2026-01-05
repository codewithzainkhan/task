from pydantic import BaseModel
from typing import List


class UserCreate(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TagSchema(BaseModel):
    name: str
    model_config = {"from_attributes": True}


class NoteCreate(BaseModel):
    title: str
    content: str
    tags: List[str] = []


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    tags: List[TagSchema]

    model_config = {"from_attributes": True}
