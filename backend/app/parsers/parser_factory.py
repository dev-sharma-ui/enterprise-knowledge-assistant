from app.parsers.pdf_parser import PDFParser
from app.parsers.docx_parser import DOCXParser
from app.parsers.txt_parser import TXTParser


class ParserFactory:

    _parsers = {
        "application/pdf": PDFParser(),
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": DOCXParser(),
        "text/plain": TXTParser(),
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
    
    