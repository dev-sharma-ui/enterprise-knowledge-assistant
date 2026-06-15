from pydantic import BaseModel

from app.schemas.document import (
    DocumentResponse
)


class DocumentProcessingResponse(
    BaseModel
):
    message: str

    document: DocumentResponse

    character_count: int

    word_count: int

    extraction_method: str