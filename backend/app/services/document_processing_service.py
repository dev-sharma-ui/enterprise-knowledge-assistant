from pathlib import Path

from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.document_content import (
    DocumentContent
)
from app.models.enums import (
    DocumentStatus
)

from app.parsers.parser_factory import (
    ParserFactory
)

from app.services.document_content_service import (
    DocumentContentService
)


class DocumentProcessingService:

    @staticmethod
    def process_document(
        db: Session,
        document: Document
    ) -> DocumentContent:

        existing_content = (
            DocumentContentService.get_by_document_id(
                db,
                document.id
            )
        )

        if existing_content:
            return existing_content

        try:

            document.status = (
                DocumentStatus.PROCESSING
            )

            file_path = Path(
                document.file_path
            )

            if not file_path.exists():

                raise FileNotFoundError(
                    f"File not found: {file_path}"
                )

            parser = (
                ParserFactory.get_parser(
                    document.content_type
                )
            )

            raw_text = (
                parser.extract_text(
                    str(file_path)
                )
            )

            if not raw_text.strip():

                raise ValueError(
                    "Document contains no extractable text."
                )

            content = DocumentContent(
                document_id=document.id,

                raw_text=raw_text,

                character_count=len(
                    raw_text
                ),

                word_count=len(
                    raw_text.split()
                ),

                extraction_method=(
                    ParserFactory.get_extraction_method(
                        document.content_type
                    )
                )
            )

            saved_content = (
                DocumentContentService.create_content(
                    db,
                    content
                )
            )

            document.status = (
                DocumentStatus.PROCESSED
            )

            db.commit()
            db.refresh(document)
            db.refresh(saved_content)

            return saved_content

        except Exception:

            db.rollback()

            document.status = (
                DocumentStatus.FAILED
            )

            db.add(document)

            db.commit()

            raise