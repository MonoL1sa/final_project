from database import Base, engine, SessionLocal
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from table_post import Post
from table_user import User

session = SessionLocal()

class Feed(Base):
    __tablename__ = "feed_action"
    post_id = Column(Integer, ForeignKey(Post.id), primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    action = Column(String)
    time = Column(DateTime)
    post = relationship("Post")
    user = relationship("User")


if __name__ == "__main__":
    Base.metadata.create_all(engine)