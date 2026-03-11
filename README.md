# 📚 Library Management API (FastAPI Backend)

[![Live API](https://img.shields.io/badge/Live-API-success?style=for-the-badge&logo=fastapi)](https://fastapi-project-4-library-management.onrender.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)
[![API Docs](https://img.shields.io/badge/API%20Docs-Swagger-green?style=for-the-badge)](https://fastapi-project-4-library-management.onrender.com/docs)

A **high-performance REST API** built with **FastAPI** for managing library books, users, and borrowing operations.

The API powers the **Library Management Dashboard** and provides endpoints for **book management, user management, borrowing operations, and analytics**.

---

# 🌐 Live API

### Base URL

https://fastapi-project-4-library-management.onrender.com

### Interactive API Documentation

Swagger UI  
https://fastapi-project-4-library-management.onrender.com/docs

ReDoc  
https://fastapi-project-4-library-management.onrender.com/redoc

---

# ✨ Features

* ⚡ **FastAPI high performance**
* 📚 **Auto-generated Swagger documentation**
* 🔄 **Complete CRUD operations**
* 📖 **Book borrowing system**
* 📊 **Library analytics endpoints**
* 🌐 **CORS enabled for frontend integration**
* 🚀 **Deployed on Render**

> Note: Data resets when the server restarts since the current version uses in-memory storage.

---

# 🏗 Architecture

Streamlit Dashboard  
│  
▼  
FastAPI Backend  
│  
▼  
In-Memory Library Store  

Future improvements could include:

* PostgreSQL database
* authentication system
* user accounts
* book reservation system

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|------|------|------|
GET | /books | Get all books |
GET | /books/{book_id} | Get a book |
GET | /books/available | Get available books |
GET | /books/borrowed | Get borrowed books |
GET | /books/category/{category} | Filter books by category |
POST | /books/add_book | Add a new book |
DELETE | /books/delete_book/{book_id} | Delete a book |
GET | /users | Get all users |
GET | /users/{user_id} | Get user |
GET | /users/{user_id}/borrowed_books | User borrowed books |
POST | /users/add_user | Add a user |
DELETE | /users/delete_user/{user_id} | Delete a user |
POST | /borrow_book | Borrow book |
POST | /return_book | Return book |
GET | /stats/library | Library statistics |
GET | /stats/books_per_category | Books per category |

---

# 📂 Project Structure

library-management-backend  
│  
├── library_api.py  
├── requirements.txt  
└── README.md  

---

# ⚙️ Local Development

Clone the repository

git clone https://github.com/iqroguerex-cpu/library-management-backend

Navigate to project

cd library-management-backend

Install dependencies

pip install -r requirements.txt

Run server

uvicorn library_api:app --reload

Open API documentation

http://127.0.0.1:8000/docs

---

# 🔗 Frontend Dashboard

Frontend Repository  
https://github.com/iqroguerex-cpu/library-management-frontend

Live Dashboard  
https://librarymanagementbychinmay.streamlit.app/

---

# 📄 License

This project is released under the **MIT License**.

---

# 👨‍💻 Author

**Chinmay V Chatradamath**

GitHub  
https://github.com/iqroguerex-cpu

---

⭐ If you found this project useful, consider **starring the repository**.
