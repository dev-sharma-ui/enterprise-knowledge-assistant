from app.parsers.pdf_parser import PDFParser
from app.parsers.docx_parser import DOCXParser
from app.parsers.txt_parser import TXTParser


class ParserFactory:

    _parsers = {
        "application/pdf": PDFParser(),
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": DOCXParser(),
        "text/plain": TXTParser(),
    }

    _extraction_methods = {
        "application/pdf": "pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "docx",
        "text/plain": "txt",
    }

    @classmethod
    def get_parser(
        cls,
        content_type: str
    ):
        parser = cls._parsers.get(content_type)

        if parser is None:
            raise ValueError(
                f"Unsupported content type: {content_type}"
            )

        return parser

    @classmethod
    def get_extraction_method(
        cls,
        content_type: str
    ) -> str:

        extraction_method = (
            cls._extraction_methods.get(
                content_type
            )
        )

        if extraction_method is None:
            raise ValueError(
                f"Unsupported content type: {content_type}"
            )

        return extraction_method