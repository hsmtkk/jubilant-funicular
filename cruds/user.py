from sqlalchemy.orm import Session

import models.user
import schemas.user


def list(db: Session) -> list[models.user.User]:
    return db.query(models.user.User).all()


def create(db: Session, user: schemas.user.UserCreate) -> models.user.User:
    new_user = models.user.User()
    db.add(new_user)
    db.commit()
    db.flush(new_user)
    return new_user
