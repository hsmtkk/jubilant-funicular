from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import cruds.todo
from routers.db import get_db
import schemas.todo

router = APIRouter(prefix="/todos")


@router.get("/", response_model=list[schemas.todo.Todo])
def list(db: Session = Depends(get_db)) -> list[schemas.todo.Todo]:
    return cruds.todo.list(db)


@router.post("/", response_model=schemas.todo.Todo)
def create(
    todo: schemas.todo.TodoCreate, db: Session = Depends(get_db)
) -> schemas.todo.Todo:
    return cruds.todo.create(db, todo)
