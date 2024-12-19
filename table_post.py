from database import Base, engine, SessionLocal
from sqlalchemy import Column, Integer, String

session = SessionLocal()

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    results = (
        session.query(Post.id)
        .filter(Post.topic == 'business')
        .order_by(Post.id.desc())
        .limit(10)
        .all()
        )
    ids_list = [id for (id,) in results]
    print(ids_list)