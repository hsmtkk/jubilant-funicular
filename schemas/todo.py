from pydantic import BaseModel


class TodoCreate(BaseModel):
    pass

    class Config:
        orm_mode = True


class Todo(TodoCreate):
    id: int
