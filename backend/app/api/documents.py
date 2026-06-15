from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    HTTPException,
    UploadFile,
    status,
)

from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.db.session import get_db

from app.models.document import Document
from app.models.enums import (
    DocumentStatus,
    DocumentVisibility,
)
from app.models.user import User

from app.schemas.document import (
    DocumentResponse,
    DocumentUploadResponse,
    DocumentDeleteResponse,
    DocumentProcessingResponse,
)

from app.services.document_service import (
    DocumentService,
)

from app.services.document_processing_service import (
    DocumentProcessingService,
)

from app.services.file_service import (
    FileService,
)


router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.get(
    "",
    response_model=list[DocumentResponse]
)
def get_documents(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    return DocumentService.get_user_documents(
        db,
        current_user.id
    )


@router.post(
    "/upload",
    response_model=DocumentUploadResponse,
    status_code=status.HTTP_201_CREATED
)
def upload_document(
    title: str = Form(...),
    visibility: DocumentVisibility = Form(
        DocumentVisibility.PRIVATE
    ),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    file_metadata = (
        FileService.save_file(file)
    )

    try:

        document = Document(
            user_id=current_user.id,
            title=title,
            original_filename=file.filename,
            stored_filename=file_metadata[
                "stored_filename"
            ],
            file_path=file_metadata[
                "file_path"
            ],
            file_size=file_metadata[
                "file_size"
            ],
            content_type=file.content_type,
            visibility=visibility,
            status=DocumentStatus.UPLOADED,
        )

        document = (
            DocumentService.create_document(
                db,
                document
            )
        )

        return {
            "message":
                "Document uploaded successfully",
            "document": document
        }

    except Exception:

        FileService.delete_file(
            file_metadata["file_path"]
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to upload document"
        )


@router.get(
    "/{document_id}",
    response_model=DocumentResponse
)
def get_document(
    document_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    document = (
        DocumentService.get_user_document(
            db,
            document_id,
            current_user.id
        )
    )

    if not document:

        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return document


@router.post(
    "/{document_id}/process",
    response_model=DocumentProcessingResponse
)
def process_document(
    document_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    document = (
        DocumentService.get_user_document(
            db,
            document_id,
            current_user.id
        )
    )

    if not document:

        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    try:

        content = (
            DocumentProcessingService
            .process_document(
                db,
                document
            )
        )

        db.refresh(document)

        return {
            "message":
                "Document processed successfully",

            "document":
                document,

            "character_count":
                content.character_count,

            "word_count":
                content.word_count,

            "extraction_method":
                content.extraction_method,
        }

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Failed to process document"
        )


@router.delete(
    "/{document_id}",
    response_model=DocumentDeleteResponse
)
def delete_document(
    document_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    document = (
        DocumentService.get_user_document(
            db,
            document_id,
            current_user.id
        )
    )

    if not document:

        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    FileService.delete_file(
        document.file_path
    )

    DocumentService.delete_document(
        db,
        document
    )

    return {
        "message":
            "Document deleted successfully"
    }