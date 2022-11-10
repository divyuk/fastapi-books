from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional

app = FastAPI()

class Book(BaseModel):
    """
    This class has the data validation schema extending the BaseModel of pydantic.
    But we can also send the empty string and that will also be acceptable parameters therefore we will use Fields for further validation.
    """
    id : UUID
    title : str = Field(min_length=1)
    author : str = Field(min_length=1,max_length=100)
    description :Optional[str] = Field(title="Desciption of the bool", max_length=100, min_length=1)
    rating : int = Field(gt=-1,lt=101)

BOOKS = []

@app.get("/")
async def read_all_books():
    if len(BOOKS)<1:
        create_books_no_api()
    return BOOKS

@app.post("/")
async def create_book(book:Book):
    BOOKS.append(book)
    return book

def create_books_no_api():
    book_1 = Book(id="cadb9626-3bad-42e6-8c47-23837b1b9194",
                  title="Sapiens",
                  author="Yuval",
                  description="A brief history of humans",
                  rating = 80)
    book_2 = Book(id="3ee0e959-27b6-4bd2-bef4-137bd3a1a62c",
                  title="Deep Work",
                  author="Cal Newport",
                  description="Works of work",
                  rating = 79)
    book_3 = Book(id="c24a270e-fb1e-491d-ac8e-36d8e6528964",
                  title="Why we Sleep",
                  author="Mathhew",
                  description="Sleep better",
                  rating = 75)
    book_4 = Book(id="71d5b4cc-a647-4da8-b949-b18dd492f0da",
                  title="Mindset",
                  author="Carol",
                  description="A little change can do magnificient change",
                  rating = 78)
    
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)