from pydantic import BaseModel, Field
from datetime import datetime

class UserGet(BaseModel):
    id: int
    age: int
    city: str
    country: str
    exp_group: int
    gender: int
    os: str
    source: str

    class Config:
        orm_mode = True

class PostGet(BaseModel):
    id: int
    text: str
    topic: str

    class Config:
        orm_mode = True

class FeedGet(BaseModel):
    post_id: int
    user_id: int
    action: str
    time: datetime
    user: UserGet
    post: PostGet

    class Config:
        orm_mode = True