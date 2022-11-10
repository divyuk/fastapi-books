from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID

app = FastAPI()

class Book(BaseModel):
    """
    This class has the data validation schema extending the BaseModel of pydantic
    """
    id : UUID
    title : str
    author : str
    description : str
    rating : str

BOOKS = []

@app.get("/")
async def read_all_books():
    return BOOKS

@app.post("/")
async def create_book(book:Book):
    BOOKS.append(book)
    return book