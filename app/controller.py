from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal

app = FastAPI(title="Livros API")

# Dependency: cria uma sessão por request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/books", response_model=list[schemas.BookRead])
def list_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_books(db, skip, limit)

@app.get("/books/{book_id}", response_model=schemas.BookRead)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.post("/books", response_model=schemas.BookRead, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.put("/books/{book_id}", response_model=schemas.BookRead)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    db_book = crud.update_book(db, book_id, book)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.delete("/books/{book_id}", response_model=schemas.BookRead)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
