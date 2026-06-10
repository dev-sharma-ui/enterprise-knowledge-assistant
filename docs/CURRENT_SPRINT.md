# CURRENT SPRINT

## Sprint

Sprint 2

## Sprint Name

Authentication Foundation

---

# Sprint Goal

Build a production-grade authentication system using:

* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT
* Password Hashing
* Dependency Injection

---

# Completed

Infrastructure

✓ FastAPI

✓ Docker

✓ PostgreSQL

✓ SQLAlchemy

✓ Alembic

✓ User Table

---

# Current Blocker

bcrypt 5.0.0

passlib 1.7.4

Compatibility issue preventing password hashing.

---

# Current Task

Fix password hashing stack.

---

# Immediate Next Tasks

1. Resolve bcrypt issue
2. Test password hashing
3. Test password verification
4. Test JWT creation
5. Create schemas
6. Create auth service
7. Create register endpoint
8. Create login endpoint

---

# Important Commands

Start PostgreSQL:

docker compose up -d

Run FastAPI:

uvicorn app.main:app --reload

Generate Migration:

alembic revision --autogenerate -m "message"

Apply Migration:

alembic upgrade head

Check PostgreSQL:

docker exec -it eka_postgres psql -U postgres -d eka_db

---

# Important Files

app/core/config.py

app/core/logger.py

app/core/security.py

app/db/session.py

app/models/user.py

alembic/env.py

---

# Definition of Done

Sprint completes only when:

✓ Register endpoint works

✓ Login endpoint works

✓ JWT generated

✓ Passwords hashed

✓ Protected endpoint works

✓ Current user dependency works
