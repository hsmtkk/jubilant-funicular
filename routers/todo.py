from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import cruds.todo
from routers import get_db
import schemas.todo

router = APIRouter(prefix="/todos")


@router.get("/", response_model=list[schemas.todo.Todo])
def list(db: Session = Depends(get_db)):
    pass
