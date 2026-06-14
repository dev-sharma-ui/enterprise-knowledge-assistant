from pathlib import Path
from uuid import uuid4
from pathlib import Path
from fastapi import UploadFile

from app.core.config import settings


class FileService:

    @staticmethod
    def ensure_upload_directory() -> Path:

        upload_dir = Path(settings.UPLOAD_DIR)

        upload_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        return upload_dir

    @staticmethod
    def generate_filename(
        original_filename: str
    ) -> str:

        extension = Path(
            original_filename
        ).suffix

        return f"{uuid4()}{extension}"

    @staticmethod
    def save_file(
        file: UploadFile
    ) -> dict:

        upload_dir = (
            FileService.ensure_upload_directory()
        )

        stored_filename = (
            FileService.generate_filename(
                file.filename
            )
        )

        file_path = (
            upload_dir / stored_filename
        )

        file_size = 0

        with open(
            file_path,
            "wb"
        ) as buffer:

            while chunk := file.file.read(
                1024 * 1024
            ):

                file_size += len(chunk)

                buffer.write(chunk)

        return {
            "stored_filename": stored_filename,
            "file_path": str(file_path),
            "file_size": file_size
        }
    
    @staticmethod
    def delete_file(
        file_path: str
    ) -> None:

        path = Path(file_path)

        if path.exists():
            path.unlink()