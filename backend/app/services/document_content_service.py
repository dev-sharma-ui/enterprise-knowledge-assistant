from sqlalchemy.orm import Session

from app.models.document_content import (
    DocumentContent
)


class DocumentContentService:

    @staticmethod
    def create_content(
        db: Session,
        content: DocumentContent
    ) -> DocumentContent:

        db.add(content)

        db.commit()

        db.refresh(content)

        return content

    @staticmethod
    def get_by_document_id(
        db: Session,
        document_id: str
    ) -> DocumentContent | None:

        return (
            db.query(DocumentContent)
            .filter(
                DocumentContent.document_id
                == document_id
            )
            .first()
        )