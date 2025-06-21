from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import database, crud, schemas

router = APIRouter()

@router.get("/todos/", response_model=list[schemas.TodoRead])
def read_todos(db: Session = Depends(database.get_db)):
    return crud.get_all_todos(db)

@router.post("/todos/", response_model=schemas.TodoRead)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(database.get_db)):
    return crud.create_todo(db, todo)

@router.put("/todos/{todo_id}", response_model=schemas.TodoRead)
def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(database.get_db)):
    return crud.update_todo(db, todo_id, todo)

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_todo(db, todo_id)
