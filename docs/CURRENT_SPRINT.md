# CURRENT SPRINT

## Sprint

Sprint 3

## Sprint Name

Knowledge Repository Foundation

---

# Sprint Goal

Build the foundational enterprise knowledge repository that future document processing, embedding generation, retrieval, authorization, and RAG pipelines will use.

This sprint is NOT focused on building a complete enterprise IAM or RBAC system.

This sprint is focused on designing a future-proof document architecture that supports:

* Document Storage
* Metadata Management
* Processing Lifecycle Tracking
* Future Authorization
* Future Retrieval Pipelines

---

# Previous Sprint

Sprint 2

Authentication Foundation

Status: COMPLETED

---

# Completed Features

Infrastructure

✓ FastAPI

✓ Docker

✓ PostgreSQL

✓ SQLAlchemy

✓ Alembic

✓ User Model

✓ Authentication System

✓ Registration

✓ Login

✓ JWT Authentication

✓ Protected Routes

✓ Current User Dependency

---

# Architectural Direction

The project is evolving toward a true Enterprise Knowledge Assistant.

Future versions will support:

* Enterprise Knowledge Bases
* Authorization-Aware Retrieval
* Role-Based Access
* Department-Level Access
* Document Visibility Controls

However, Sprint 3 intentionally focuses on repository foundations rather than full enterprise authorization.

---

# Current Task

Design and implement the document repository layer.

---

# Sprint Deliverables

## Database

* Document Model
* User ↔ Document Relationship
* Visibility Field
* Processing Status Field
* Alembic Migration

## Schemas

* DocumentCreate
* DocumentResponse
* DocumentListResponse

## Services

* Document Service Layer

## API

POST /documents/upload

GET /documents

GET /documents/{document_id}

DELETE /documents/{document_id}

---

# Document Fields Planned

* id
* title
* original_filename
* stored_filename
* file_path
* file_size
* content_type
* uploaded_by
* visibility
* status
* created_at
* updated_at

---

# Visibility Options

private

organization

---

# Processing Status Options

uploaded

processing

processed

failed

---

# Why These Fields Exist

visibility:

Future support for enterprise authorization.

status:

Future support for:

PDF Parsing

Chunking

Embeddings

Qdrant Indexing

RAG Processing

without schema redesign.

---

# Future Pipeline

Document Upload
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
Qdrant
↓
Hybrid Retrieval
↓
Re-ranking
↓
RAG Response

---

# Definition Of Done

Sprint 3 completes only when:

✓ Document model exists

✓ User relationship exists

✓ Migration applied

✓ Upload endpoint works

✓ Metadata stored

✓ Document listing works

✓ Document retrieval works

✓ Processing status tracked

✓ Visibility field implemented
