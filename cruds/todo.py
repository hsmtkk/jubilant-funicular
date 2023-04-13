from sqlalchemy.orm import Session

import models.todo


def list(db: Session) -> list[models.todo.Todo]:
    return db.query(models.todo.Todo).all()
