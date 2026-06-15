from app.parsers.base_parser import BaseParser


class TXTParser(BaseParser):

    def extract_text(
        self,
        file_path: str
    ) -> str:

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                return file.read().strip()

        except UnicodeDecodeError:

            with open(
                file_path,
                "r",
                encoding="latin-1"
            ) as file:

                return file.read().strip()