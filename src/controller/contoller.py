from src.controller.abc import IController, AController
from src.google_sheets.abc import IGoogleTable
from src.parser.abc import IParser
from src.schemes.product import ProductSchema


class Controller(IController, AController):
    @staticmethod
    async def get_data_by_key_word(key_word: str, parser: IParser, table: IGoogleTable):
        parse_result: list[ProductSchema] = await parser.run(key_word)
        table.send(parse_result)