from pydantic import BaseModel


class UserCreate(BaseModel):
    pass

    class Config:
        orm_mode = True


class User(UserCreate):
    id: int
