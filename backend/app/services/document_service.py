from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentService:

    @staticmethod
    def create_document(
        db: Session,
        document: Document
    ) -> Document:

        db.add(document)
        db.commit()
        db.refresh(document)

        return document

    @staticmethod
    def get_document_by_id(
        db: Session,
        document_id: str
    ) -> Document | None:

        return (
            db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

    @staticmethod
    def get_user_documents(
        db: Session,
        user_id: str
    ) -> list[Document]:

        return (
            db.query(Document)
            .filter(Document.user_id == user_id)
            .order_by(Document.created_at.desc())
            .all()
        )

    @staticmethod
    def delete_document(
        db: Session,
        document: Document
    ) -> None:

        db.delete(document)
        db.commit()

    @staticmethod
    def get_user_document(
        db: Session,
        document_id: str,
        user_id: str
    ) -> Document | None:

        return (
            db.query(Document)
            .filter(
                Document.id == document_id,
                Document.user_id == user_id
            )
            .first()
        )