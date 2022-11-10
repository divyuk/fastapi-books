from fastapi import FastAPI

app = FastAPI()
BOOKS = {
    'book_1' : {'title' : 'Sapiens', 'author' : 'Yuval Noah Harari'}, 
    'book_2' : {'title' : 'Deep Work', 'author' : 'Cal Newport'}, 
    'book_3' : {'title' : 'Why we Sleep', 'author':'Matthew Walker'}, 
    'book_4' : {'title' : 'Mindset', 'author':'Carol'},
    'book_5' : {'title' : 'Hyperfocus', 'author':'Chris Bailey'},
}

@app.get("/")
async def read_all_books():
    return BOOKS