from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BOOKS = [
    {"id": 1, "title": "Clean Code", "author": "Robert Martin", "category": "programming", "available": True},
    {"id": 2, "title": "Atomic Habits", "author": "James Clear", "category": "self-help", "available": True},
    {"id": 3, "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "category": "programming", "available": True}
]

USERS = [
    {"id": 1, "name": "Alice", "borrowed_books": []},
    {"id": 2, "name": "Bob", "borrowed_books": []}
]

@app.get("/books")
async def get_books():
    return BOOKS

@app.get("/users")
async def get_users():
    return USERS

@app.post("/books/add_book")
async def add_book(book = Body()):
    for b in BOOKS:
        if b["id"] == book["id"]:
            return {"message": "Book ID already exists"}
    BOOKS.append(book)
    return {"message": "Book Added Successfully"}

@app.post("/users/add_user")
async def add_user(user = Body()):
    for u in USERS:
        if u["id"] == user["id"]:
            return {"message": "User ID already exists"}
    USERS.append(user)
    return {"message": "User Added Successfully"}

@app.post("/borrow_book")
async def borrow_book(user_id: int, book_id: int):
    for user in USERS:
        if user["id"] == user_id:
            for book in BOOKS:
                if book["id"] == book_id:
                    if not book["available"]:
                        return {"message": "Book Not Available"}
                    user["borrowed_books"].append(book_id)
                    book["available"] = False
                    return {"message": "Book Borrowed Successfully"}
            return {"message": "Book ID Invalid"}
    return {"message": "User ID Invalid"}

@app.post("/return_book")
async def return_book(user_id: int, book_id: int):
    for user in USERS:
        if user["id"] == user_id:
            if book_id in user["borrowed_books"]:
                for book in BOOKS:
                    if book["id"] == book_id:
                        user["borrowed_books"].remove(book_id)
                        book["available"] = True
                        return {"message": "Book Returned Successfully"}
                return {"message": "Book ID Invalid"}
            return {"message": "User did not borrow this book"}
    return {"message": "User ID Invalid"}
