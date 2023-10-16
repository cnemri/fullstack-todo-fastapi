from sqlalchemy.orm import Session
import schemas, models


def create_todo(db: Session, todo: schemas.ToDoRequest):
    db_todo = models.ToDo(
        name=todo.name,
        completed=todo.completed,
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def read_todos(db: Session, completed: bool):
    if completed is None:
        return db.query(models.ToDo).all()
    return db.query(models.ToDo).filter(models.ToDo.completed == completed).all()


def read_todo(db: Session, todo_id: int):
    return db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()


def update_todo(db: Session, todo_id: int, todo: schemas.ToDoRequest):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if todo.name is None:
        return None
    db_todo.name = todo.name
    db_todo.completed = todo.completed
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if db_todo is None:
        return None
    db.delete(db_todo)
    db.commit()
    return True
