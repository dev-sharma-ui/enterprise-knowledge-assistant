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

# ADR-011

Title:
Support Enterprise Authorization and Knowledge Visibility

Status:
Accepted

Reason:

An Enterprise Knowledge Assistant must support controlled access to documents and retrieved knowledge.

Not all documents should be visible to all users.

Examples:

* HR Policies
* Financial Reports
* Engineering SOPs
* Executive Documents

Each category may have different access requirements.

Decision:

The system will introduce authorization and visibility controls early in the architecture.

Future entities will support:

* User Roles
* Departments
* Document Visibility
* Access Policies

However, the project will initially implement a simplified single-organization architecture and progressively evolve toward full enterprise authorization.

Benefits:

* More realistic enterprise design
* Better interview discussion points
* Future support for role-based retrieval
* Future support for authorization-aware RAG

Consequences:

Additional schema fields and relationships will be introduced in future sprints.



# ADR-012

Title:
Store Extracted Raw Text Before Chunking

Status:
Accepted

Reason:

Many Retrieval-Augmented Generation systems directly parse a document and immediately generate chunks.

This approach tightly couples document parsing and chunk generation, making future improvements difficult.

Examples:

* Changing chunking strategies
* Adding metadata extraction
* Adding summarization
* Adding OCR
* Re-processing documents

would require reopening and reprocessing original files repeatedly.

Decision:

The system will introduce a dedicated DocumentContent layer.

Pipeline:

Document
↓
Text Extraction
↓
DocumentContent
↓
Chunking
↓
Embeddings
↓
Vector Database

The extracted raw text will be stored permanently in the database.

Future chunking and embedding systems will operate on stored text rather than reopening original files.

Benefits:

* Separation of concerns
* Easier reprocessing
* Faster experimentation
* Better maintainability
* Cleaner architecture
* Reduced duplicate processing

Consequences:

Additional storage requirements for extracted text.

However, the architectural benefits outweigh the storage cost.

Future Impact:

Supports:

* Multiple chunking strategies
* Metadata extraction
* Summarization
* OCR integration
* Authorization-aware retrieval
* Re-indexing without re-reading files
