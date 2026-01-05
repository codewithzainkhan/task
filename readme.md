##📝 Note Taking API – FastAPI Backend Assignment
Overview

This project is a Note Taking REST API built using FastAPI.
It allows users to securely create, manage, and organize personal notes using tags, with JWT-based authentication ensuring that only note owners can modify or delete their notes.



##🛠️ Tech Stack

Language: Python 3.9+

Framework: FastAPI

Database: SQLite

ORM: SQLAlchemy

Authentication: JWT (OAuth2 Password Flow)

Password Hashing: Passlib (bcrypt)

API Documentation: Swagger / OpenAPI

Containerization: Docker

##📦 Features
✅ Authentication

User registration

User login with JWT token

Secure password hashing

Protected routes for authenticated users

✅ Note Management (CRUD)

Create notes with title, content, and tags

Retrieve all notes for the logged-in user

Retrieve a specific note by ID

Update note title, content, and tags

Delete notes

✅ Tag Support

Notes can have multiple tags

Tags are reusable across notes

Many-to-many relationship between notes and tags

##🗂️ Project Structure
Task/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── deps.py
│   ├── auth.py
│   └── routes/
│       ├── auth.py
│       └── notes.py
├── notes.db
├── .env
├── Dockerfile
├── requirements.txt
└── README.md

##🧩 Database Design
User
Field	Type
id	Integer (Primary Key)
username	String (Unique)
email	String (Unique)
hashed_password	String

Note
Field	Type
id	Integer (Primary Key)
title	String
content	Text
owner_id	Foreign Key (User)
created_at	Timestamp
updated_at	Timestamp

Tag
Field	Type
id	Integer (Primary Key)
name	String (Unique)
Relationships

User → Notes: One-to-Many

Notes ↔ Tags: Many-to-Many via association table

##🚀 Local Setup Instructions

1️⃣ Clone the Repository
git clone <repository-url>
cd Task

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

##🗄️ Database Setup

The project uses SQLite

Database tables are created automatically at startup using SQLAlchemy:

Base.metadata.create_all(bind=engine)


No Alembic migrations are used

▶️ Run the Application (Local)
uvicorn app.main:app --reload


The API will be available at:

http://127.0.0.1:8000

📘 API Documentation

FastAPI provides interactive documentation automatically:

Swagger UI:
👉 http://127.0.0.1:8000/docs

ReDoc:
👉 http://127.0.0.1:8000/redoc

##🔐 Authentication Flow

Register a user

POST /auth/register


Login to receive JWT token

POST /auth/login


Authorize requests

Authorization: Bearer <access_token>


All note endpoints require authentication.

🧪 API Endpoints
Authentication
Method	Endpoint	Description
POST	/auth/register	Register new user
POST	/auth/login	Login and receive JWT
Notes
Method	Endpoint	Description
POST	/notes/	Create a note
GET	/notes/	List user notes
GET	/notes/{id}	Retrieve a note
PUT	/notes/{id}	Update a note
DELETE	/notes/{id}	Delete a note

##🐳 Docker Support

This project includes Docker support for easy setup and consistent execution.

📦 Requirements

Docker installed
👉 https://docs.docker.com/get-docker/

▶️ Build Docker Image
docker build -t note-taking-api .

▶️ Run Docker Container
docker run -d \
  -p 8000:8000 \
  --name note-taking-api \
  note-taking-api


API will be available at:

http://localhost:8000

📘 API Docs (Docker)

Swagger: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

🗄️ SQLite Behavior in Docker

SQLite database is created inside the container

Data persists only while the container exists

Optional: Persistent Database
docker run -d \
  -p 8000:8000 \
  -v $(pwd)/notes.db:/app/notes.db \
  --name note-taking-api \
  note-taking-api

🧹 Stop & Remove Container
docker stop note-taking-api
docker rm note-taking-api

⚙️ Environment Configuration

Environment variables are loaded from .env.

Example:

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

##🎯 Task Compliance

✔ CRUD operations implemented
✔ Tag support with many-to-many relationship
✔ JWT authentication implemented
✔ SQLAlchemy ORM usage
✔ Docker support included
✔ Clean code separation and documentation