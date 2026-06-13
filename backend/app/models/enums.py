from enum import Enum


class DocumentVisibility(str, Enum):
    PRIVATE = "private"
    ORGANIZATION = "organization"


class DocumentStatus(str, Enum):
    UPLOADED = "uploaded"
    PROCESSING = "processing"
    PROCESSED = "processed"
    FAILED = "failed"