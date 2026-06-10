# Architecture Decisions Log

This document records important technical decisions made during development.

---

# ADR-001

Title:
Use FastAPI Instead of Django

Status:
Accepted

Reason:

The project is API-centric and Machine Learning focused.

FastAPI provides:

* High performance
* Native async support
* Automatic OpenAPI documentation
* Better integration with AI services

Consequences:

Pros:

* Faster development
* Cleaner API architecture
* Better ML integration

Cons:

* Fewer built-in features than Django

---

# ADR-002

Title:
Use PostgreSQL Instead of MongoDB

Status:
Accepted

Reason:

The system contains highly relational data.

Examples:

Users
→ Documents
→ Chunks
→ Conversations
→ Messages

Relational databases fit naturally.

Consequences:

Pros:

* Strong consistency
* Powerful joins
* Mature ecosystem

Cons:

* More schema management

---

# ADR-003

Title:
Use SQLAlchemy 2.0

Status:
Accepted

Reason:

Industry standard ORM.

Provides:

* Type-safe models
* Relationships
* Migration support
* Long-term maintainability

---

# ADR-004

Title:
Use Docker for Local Development

Status:
Accepted

Reason:

Ensures identical environments across machines.

Benefits:

* Reproducibility
* Easier onboarding
* Cleaner deployment path

---

# ADR-005

Title:
Use Qdrant as Vector Database

Status:
Accepted

Reason:

Open-source vector database with strong performance and easy deployment.

Alternatives Considered:

* Pinecone
* Weaviate
* Chroma

Decision:

Qdrant selected.

---

# ADR-006

Title:
Use Hybrid Retrieval

Status:
Accepted

Components:

* Dense Retrieval
* BM25 Retrieval

Reason:

Semantic retrieval alone misses keyword matches.

BM25 alone misses semantic similarity.

Hybrid retrieval provides better recall.

---

# ADR-007

Title:
Use Cross Encoder Re-ranking

Status:
Accepted

Reason:

Improves retrieval precision before sending context to the LLM.

Expected Model:

cross-encoder/ms-marco-MiniLM-L-6-v2

---

# ADR-008

Title:
Use Dedicated Service Layer

Status:
Accepted

Reason:

Business logic should not live inside API routes.

Benefits:

* Cleaner code
* Easier testing
* Better maintainability

---

# ADR-009

Title:
Use Configuration Layer

Status:
Accepted

Reason:

Centralized management of:

* Database URLs
* API Keys
* Secrets
* Environment Variables

---

# ADR-010

Title:
Follow Enterprise Folder Structure

Status:
Accepted

Reason:

The project is intended to demonstrate production-grade engineering practices.

Goal:

Scalable architecture supporting thousands of lines of code without major refactoring.
