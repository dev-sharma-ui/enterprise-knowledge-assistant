from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
    String,
    Text,
    Integer,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.db.base import Base


class DocumentContent(Base):
    __tablename__ = "document_contents"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4())
    )

    document_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey(
            "documents.id",
            ondelete="CASCADE"
        ),
        nullable=False,
        unique=True,
        index=True
    )

    raw_text: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    character_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    word_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    extraction_method: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    document = relationship(
        "Document",
        back_populates="document_content"
    )