from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Post
from schemas import PostCreate
from dependencies import get_current_user, get_db

router = APIRouter()

@router.get("/")
def get_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()

@router.post("/")
def create_post(post: PostCreate, user=Depends(get_current_user), db: Session = Depends(get_db)):
    new_post = Post(
        title=post.title,
        content=post.content,
        user_id=user.id
    )
    db.add(new_post)
    db.commit()
    return new_post

@router.delete("/{post_id}")
def delete_post(post_id: int, user=Depends(get_current_user), db: Session = Depends(get_db)):
    post = db.query(Post).get(post_id)

    if not post:
        raise HTTPException(status_code=404)

    if post.user_id != user.id and user.role != "moderator":
        raise HTTPException(status_code=403)

    db.delete(post)
    db.commit()
    return {"msg": "Deleted"}
