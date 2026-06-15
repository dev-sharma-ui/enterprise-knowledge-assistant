import fitz

from app.parsers.base_parser import BaseParser


class PDFParser(BaseParser):

    def extract_text(
        self,
        file_path: str
    ) -> str:

        text_parts = []

        with fitz.open(file_path) as pdf:

            for page in pdf:

                text_parts.append(
                    page.get_text()
                )

        return "\n".join(text_parts).strip()