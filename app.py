from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import func

from table_post import Post
from table_user import User
from table_feed import Feed
from schema import UserGet, PostGet, FeedGet

from database import SessionLocal

app = FastAPI()

def get_db():
    with SessionLocal() as db:
        return db


@app.get("/user/{id}", response_model=UserGet)
def user_get(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/post/{id}", response_model=PostGet)
def post_get(id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.get("/user/{id}/feed", response_model=List[FeedGet])
def user_feed(id: int, limit: int = Query(10, le=100),db: Session = Depends(get_db)):
    feeds = db.query(Feed).filter(Feed.user_id == id).order_by(Feed.time.desc()).limit(limit).all()
    return feeds

@app.get("/post/{id}/feed", response_model=List[FeedGet])
def post_feed(id: int, limit: int = Query(10, le=100), db: Session = Depends(get_db)):
    feeds = db.query(Feed).filter(Feed.post_id == id).order_by(Feed.time.desc()).limit(limit).all()
    return feeds

@app.get("/post/recommendations/", response_model=List[PostGet])
def get_recommended_feed(limit: int = Query(10, le=100), db: Session = Depends(get_db)):
    posts_with_likes = (
        db.query(Post)
        .select_from(Feed)
        .join(Post, Feed.post_id == Post.id)
        .group_by(Post.id)
        .order_by(func.count(Feed.post_id).desc())
        .limit(limit)
        .all()
    )
    return [PostGet(id=post.id, text=post.text, topic=post.topic) for post in posts_with_likes]