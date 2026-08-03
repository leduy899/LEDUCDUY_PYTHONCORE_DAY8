from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import BookResponse, BookCreate
from models import BookModel
from database import engine, get_db, Base

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Library Management API")

@app.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(BookModel).filter(BookModel.code == book.code).first()
    if db_book:
        raise HTTPException(status_code=400, detail="Mã sách (code) đã tồn tại!")
    new_book = BookModel(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book
@app.get("/books", response_model=BookResponse, status_code=status.HTTP_200_OK)
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = db.query(BookModel).offset(skip).limit(limit).all()
    return books
