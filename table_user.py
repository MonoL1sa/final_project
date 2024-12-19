from database import Base, engine, SessionLocal
from sqlalchemy import Column, Integer, String, func

session = SessionLocal()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    city = Column(String)
    country = Column(String)
    exp_group = Column(Integer)
    gender = Column(Integer)
    os = Column(String)
    source = Column(String)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    user_results = (
        session.query(User.country, User.os, func.count().label('count'))
        .filter(User.exp_group == 3)
        .group_by(User.country, User.os)
        .having(func.count() > 100)
        .order_by(func.count().desc())
        .all()
    )
    pairs_list = [(country, os, count) for country, os, count in user_results]
    print(pairs_list)