# FastAPI Backend

A collection of backend engineering projects and exercises built with FastAPI,
covering REST API design, request/response validation, database integration,
authentication, and deployment.

## Overview

This repo tracks progressive backend development work — starting from core
API fundamentals and building toward a fully deployed, database-backed
service with authentication and containerised deployment. Each folder
represents a stage of that progression, moving from isolated concepts toward
an integrated, production-style application.

## Stack

- **Framework:** FastAPI
- **Server:** Uvicorn (ASGI)
- **Database:** PostgreSQL
- **ORM / Migrations:** SQLAlchemy, Alembic
- **Auth:** Password hashing, JWT-based authentication
- **Containerisation:** Docker
- **Deployment:** Railway / Render

## Structure

fastapi-backend/

├── week-5/   FastAPI fundamentals — routes, path operations, Pydantic

├── week-6/   Path & query params, status codes, validation, middleware

├── week-7/   PostgreSQL — schema design, raw SQL, psycopg2

├── week-8/   SQLAlchemy ORM — models, sessions, relationships, migrations

├── week-9/   FastAPI + PostgreSQL — full CRUD against a real database

├── week-10/  Auth — password hashing, JWT, protected routes

├── week-11/  Docker — containerising the application

├── week-12/  Deployment — first live, publicly accessible project

└── README.md

Each folder is largely self-contained, with its own scripts and (where
applicable) a `requirements.txt`. Later folders build on patterns introduced
earlier — e.g. the database integration in `week-9` reuses the routing
conventions established in `week-5` and `week-6`.

## How to run

From the relevant folder:

```bash
python -m pip install -r requirements.txt
python -m uvicorn <filename>:app --reload
```

Then open `http://127.0.0.1:8000/docs` for the interactive Swagger UI, or
`http://127.0.0.1:8000/redoc` for ReDoc.

For folders involving a database, set the required environment variables
(e.g. `DATABASE_URL`) before starting the server — see that folder's own
notes if present.

## Status

🚧 Active development — currently on FastAPI fundamentals, with PostgreSQL
integration, authentication, and deployment to follow.