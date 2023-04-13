from sqlalchemy.orm import Session

import models.todo
import schemas.todo


def list(db: Session) -> list[models.todo.Todo]:
    return db.query(models.todo.Todo).all()


def create(db: Session, todo: schemas.todo.TodoCreate) -> models.todo.Todo:
    new_todo = models.todo.Todo(
        user_id=todo.user_id,
    )
    db.add(new_todo)
    db.commit()
    db.flush(new_todo)
    return new_todo
