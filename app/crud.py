from sqlalchemy.orm import Session
from . import models, schemas

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, take: int = 100):
    return db.query(models.Book).offset(skip).limit(take).all()

def create_book(db: Session, book: schemas.BookCreate):
    data = book.model_dump() # representação em formato de dicionário 
    db_book = models.Book(**data) # transforma em objeto ORM
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db:Session, book_id: int):
    db_book = get_book(db, book_id)
    if not db_book:
        return None
    db.delete(db_book)
    db.commit()
    return db_book

def update_book(db:Session, book_id: int, book:schemas.BookUpdate):
    db_book = get_book(db, book_id)
    if not db_book:
        return None
    update_data = book.model_dump(exclude_unset=True) #atualiza apenas campos enviados na requisicao
    for k, v in update_data.items():
        setattr(db_book, k, v)
    db.commit()
    db.refresh(db_book)
    return db_book 