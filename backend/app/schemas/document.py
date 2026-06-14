from datetime import datetime

from pydantic import BaseModel

from app.models.enums import (
    DocumentVisibility,
    DocumentStatus,
)


class DocumentResponse(BaseModel):
    id: str
    title: str

    original_filename: str

    file_size: int

    content_type: str

    visibility: DocumentVisibility

    status: DocumentStatus

    created_at: datetime

    model_config = {
        "from_attributes": True
    }


class DocumentListResponse(BaseModel):
    documents: list[DocumentResponse]


class DocumentUploadResponse(BaseModel):
    message: str

    document: DocumentResponse

class DocumentDeleteResponse(BaseModel):
    message: str