# FastAPI Notes API

A simple FastAPI backend for user authentication and note-taking, supporting JWT-based authentication and CRUD operations. Uses SQLite as the database.

---

## Features

- User registration and login (JWT authentication)
- Create, read, update, delete (CRUD) notes
- Notes are linked to authenticated users
- Interactive API docs with Swagger (`/docs`) and ReDoc (`/redoc`)
- Passwords hashed with bcrypt
- SQLite database (no Alembic)

