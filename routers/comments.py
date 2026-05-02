from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Comment
from schemas import CommentCreate
from dependencies import get_current_user, get_db

router = APIRouter()

@router.post("/{post_id}")
def create_comment(post_id: int, comment: CommentCreate, user=Depends(get_current_user), db: Session = Depends(get_db)):
    new_comment = Comment(
        content=comment.content,
        user_id=user.id,
        post_id=post_id
    )
    db.add(new_comment)
    db.commit()
    return new_comment
