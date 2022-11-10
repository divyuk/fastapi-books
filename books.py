from fastapi import FastAPI
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
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id : int):
    return  {"book_title" : book_id}

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