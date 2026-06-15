from docx import Document

from app.parsers.base_parser import BaseParser


class DOCXParser(BaseParser):

    def extract_text(
        self,
        file_path: str
    ) -> str:

        document = Document(file_path)

        text_parts = [
            paragraph.text
            for paragraph in document.paragraphs
        ]

        return "\n".join(text_parts).strip()