from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import cruds.user
from routers.db import get_db
import schemas.user

router = APIRouter(prefix="/users")


@router.get("/", response_model=list[schemas.user.User])
def list(db: Session = Depends(get_db)) -> list[schemas.user.User]:
    return cruds.user.list(db)


@router.post("/", response_model=schemas.user.User)
def create(
    user: schemas.user.UserCreate, db: Session = Depends(get_db)
) -> schemas.user.User:
    return cruds.user.create(db, user)
