from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class PostCreate(BaseModel):
    title: str
    content: str

class CommentCreate(BaseModel):
    content: str
