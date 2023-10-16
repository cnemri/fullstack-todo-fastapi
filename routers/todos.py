from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
import schemas, models, crud
from database import SessionLocal

router = APIRouter(
    prefix="/todos",
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.ToDoRequest, db: Session = Depends(get_db)):
    todo = crud.create_todo(db=db, todo=todo)
    return todo


# get todos
@router.get("", response_model=List[schemas.ToDoResponse])
def read_todos(completed: bool = None, db: Session = Depends(get_db)):
    todos = crud.read_todos(db=db, completed=completed)
    return todos


# get todo
@router.get("/{todo_id}", response_model=schemas.ToDoResponse)
def read_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.read_todo(db=db, todo_id=todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


# update todo
@router.put("/{todo_id}", response_model=schemas.ToDoResponse)
def update_todo(todo_id: int, todo: schemas.ToDoRequest, db: Session = Depends(get_db)):
    todo = crud.update_todo(db=db, todo_id=todo_id, todo=todo)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


# delete todo
@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.delete_todo(db=db, todo_id=todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
