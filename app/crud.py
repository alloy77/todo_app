from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas
from fastapi import HTTPException

def get_all_todos(db: Session):
    return db.query(models.Todo).all()

def get_todo_by_title(db: Session, title: str):
    return db.query(models.Todo).filter(func.lower(models.Todo.title) == title.lower()).first()

def create_todo(db: Session, todo: schemas.TodoCreate):
    existing = get_todo_by_title(db, todo.title)
    if existing:
        raise HTTPException(status_code=400, detail="Todo with this title already exists.")
    
    db_todo = models.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo: schemas.TodoUpdate):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    # Check for duplicate title if it's changed
    if db_todo.title.lower() != todo.title.lower():
        if get_todo_by_title(db, todo.title):
            raise HTTPException(status_code=400, detail="Another todo with this title already exists.")
    
    db_todo.title = todo.title
    db_todo.description = todo.description
    db_todo.completed = todo.completed
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"detail": "Todo deleted"}
