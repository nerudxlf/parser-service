from datetime import datetime

from fastapi import FastAPI, Depends

from setting_env import table_id, google_spreadsheets
from src.controller.abc import IController
from src.controller.contoller import Controller
from src.google_sheets.abc import IGoogleTable
from src.google_sheets.table import GoogleTable
from src.parser.abc import IParser
from src.parser.factory import ParserFactory
from src.parser.json.parser import JsonParser

app = FastAPI(title="Parser API", version="0.0.1")

controller = Controller()
parser_factory = ParserFactory()
parser_factory.register_parser("json", JsonParser)
json_parser = parser_factory.get_parser('json')
google_table = GoogleTable(table_id, [google_spreadsheets])


@app.get("/api/parser/{key_word}")
async def get_data_by_key_word(
        key_word: str,
        parser: IParser = Depends(json_parser),
        table: IGoogleTable = Depends(google_table),
        current_controller: IController = Depends(controller)):
    await current_controller.get_data_by_key_word(key_word, parser, table)
