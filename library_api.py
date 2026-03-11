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

@app.get("/books/{book_id}")
async def get_book_by_id(book_id: int):
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    return {"message": "Book Not Found"}

@app.get("/books/available")
async def available_books():
    result = []
    for book in BOOKS:
        if book["available"]:
            result.append(book)
    return result

@app.get("/books/borrowed")
async def borrowed_books():
    result = []
    for book in BOOKS:
        if not book["available"]:
            result.append(book)
    return result

@app.get("/books/category/{category}")
async def books_by_category(category: str):
    result = []
    for book in BOOKS:
        if book["category"].casefold() == category.casefold():
            result.append(book)
    return result

@app.post("/books/add_book")
async def add_book(book = Body()):
    for b in BOOKS:
        if b["id"] == book["id"]:
            return {"message": "Book ID already exists"}
    BOOKS.append(book)
    return {"message": "Book Added Successfully"}

@app.delete("/books/delete_book/{book_id}")
async def delete_book(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i]["id"] == book_id:
            if not BOOKS[i]["available"]:
                return {"message": "Cannot delete borrowed book"}
            BOOKS.pop(i)
            return {"message": "Book Deleted Successfully"}
    return {"message": "Book Not Found"}

@app.get("/users")
async def get_users():
    return USERS

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    for user in USERS:
        if user["id"] == user_id:
            return user
    return {"message": "User Not Found"}

@app.get("/users/{user_id}/borrowed_books")
async def user_borrowed_books(user_id: int):
    for user in USERS:
        if user["id"] == user_id:
            result = []
            for book in BOOKS:
                if book["id"] in user["borrowed_books"]:
                    result.append(book)
            return result
    return {"message": "User Not Found"}

@app.post("/users/add_user")
async def add_user(user = Body()):
    for u in USERS:
        if u["id"] == user["id"]:
            return {"message": "User ID already exists"}
    USERS.append(user)
    return {"message": "User Added Successfully"}

@app.delete("/users/delete_user/{user_id}")
async def delete_user(user_id: int):
    for i in range(len(USERS)):
        if USERS[i]["id"] == user_id:
            if USERS[i]["borrowed_books"]:
                return {"message": "User still has borrowed books"}
            USERS.pop(i)
            return {"message": "User Deleted Successfully"}
    return {"message": "User Not Found"}

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

@app.get("/stats/library")
async def library_stats():
    total_books = len(BOOKS)
    available_books = 0
    borrowed_books = 0
    for book in BOOKS:
        if book["available"]:
            available_books += 1
        else:
            borrowed_books += 1
    return {
        "total_books": total_books,
        "available_books": available_books,
        "borrowed_books": borrowed_books,
        "total_users": len(USERS)
    }

@app.get("/stats/books_per_category")
async def books_per_category():
    stats = {}
    for book in BOOKS:
        category = book["category"]
        if category not in stats:
            stats[category] = 0
        stats[category] += 1
    return stats
