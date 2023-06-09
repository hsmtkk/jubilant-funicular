from pydantic import BaseModel


class TodoCreate(BaseModel):
    user_id: int

    class Config:
        orm_mode = True


class Todo(TodoCreate):
    id: int
