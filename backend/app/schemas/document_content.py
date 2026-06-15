from datetime import datetime

from pydantic import BaseModel

from backend.app.schemas.document import DocumentResponse


class DocumentContentResponse(BaseModel):
    id: str

    document_id: str

    character_count: int

    word_count: int

    extraction_method: str

    created_at: datetime

    model_config = {
        "from_attributes": True
    }

class DocumentProcessResponse(BaseModel):
    message: str

    document: DocumentResponse

    content: DocumentContentResponse