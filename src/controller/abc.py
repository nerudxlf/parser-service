from src.google_sheets.abc import IGoogleTable
from src.parser.abc import IParser


class AController:
    def __call__(self):
        return self


class IController:
    @staticmethod
    async def get_data_by_key_word(key_word: str, parser: IParser, table: IGoogleTable):
        raise NotImplementedError()
