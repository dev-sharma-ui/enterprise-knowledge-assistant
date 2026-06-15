from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
    String,
    DateTime,
    BigInteger,
    ForeignKey,
    Enum,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.db.base import Base
from app.models.enums import (
    DocumentVisibility,
    DocumentStatus,
)


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4())
    )

    user_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    original_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    stored_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )

    file_path: Mapped[str] = mapped_column(
        String(1024),
        nullable=False
    )

    file_size: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False
    )

    content_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    visibility: Mapped[DocumentVisibility] = mapped_column(
        Enum(DocumentVisibility),
        default=DocumentVisibility.PRIVATE,
        nullable=False
    )

    status: Mapped[DocumentStatus] = mapped_column(
        Enum(DocumentStatus),
        default=DocumentStatus.UPLOADED,
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

    owner = relationship(
        "User",
        back_populates="documents"
    )

    document_content = relationship(
    "DocumentContent",
    back_populates="document",
    cascade="all, delete-orphan",
    uselist=False
    )
    