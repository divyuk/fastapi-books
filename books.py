from fastapi import FastAPI
from typing import Optional
from enum import Enum
app = FastAPI()
BOOKS = {
    'book_1' : {'title' : 'Sapiens', 'author' : 'Yuval Noah Harari'}, 
    'book_2' : {'title' : 'Deep Work', 'author' : 'Cal Newport'}, 
    'book_3' : {'title' : 'Why we Sleep', 'author':'Matthew Walker'}, 
    'book_4' : {'title' : 'Mindset', 'author':'Carol'},
    'book_5' : {'title' : 'Hyperfocus', 'author':'Chris Bailey'},
}

class DirectionName(str,Enum):
    north = "North"
    south = "South"
    east  = "East"
    west  = "West"

@app.get("/")
async def read_all_books(skip_book :Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS

@app.get("/books/mybook")
async def read_favourite_book():
    return {"book_title" : "My favourite book"}

@app.get("/directons/{direction_name}")
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {"Direction"  : direction_name, "sub" : "Up"}
    if direction_name == DirectionName.south:
        return {"Direction"  : direction_name, "sub" : "Down"}
    if direction_name == DirectionName.west:
        return {"Direction"  : direction_name, "sub" : "left"}
    return {"Direction"  : direction_name, "sub" : "right"}

@app.get("/particular/")
async def read_book(book_name:str):
    return BOOKS[book_name]

@app.post("/")
async def create_book(book_title,book_author):
    current_book_id = 0
    if len(BOOKS) >0:
        last_book = list(BOOKS)[-1]
        book_id = int(last_book.split('_')[-1])
        current_book_id = book_id
    BOOKS[f"book_{current_book_id+1}" ] = {"title" : book_title , "author" : book_author}
    return BOOKS[f"book_{current_book_id+1}"]

@app.put("/{book_name}")
async def update_book(book_name:str, book_title:str, book_author:str):
    book_information = {'title': book_title, 'author': book_author }
    BOOKS[book_name] = book_information
    return book_information

@app.delete("/{book_name}")
async def delete_book(book_name):
    del BOOKS[book_name]
    return f"Book {book_name} deleted"