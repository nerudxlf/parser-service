from setting_env import tablename, shopname
from src.google_sheets.abc import IGoogleTable, AGoogleTable
from src.schemes.product import ProductSchema


class GoogleTable(IGoogleTable, AGoogleTable):
    def send(self, data: list[ProductSchema]):
        body, requests = self.__header_generate(tablename)
        body, requests = self.__body_generate(body, requests, data)
        sheet = self.service.spreadsheets()
        self.__page_worker(tablename)
        result = sheet.values().batchUpdate(spreadsheetId=self.spreadsheet_id, body=body).execute()
        result = sheet.batchUpdate(spreadsheetId=self.spreadsheet_id, body=requests).execute()

    def __page_worker(self, table: str):
        sheet = self.service.spreadsheets()
        sheet.values().clear(spreadsheetId=self.spreadsheet_id, range=table, body={}).execute()

    @staticmethod
    def __body_generate(body: dict, requests: dict, data: list[ProductSchema]):
        for i, product in enumerate(data):
            body.get("data")[0].get("values").append([
                product.link,
                product.shop,
                product.name,
                product.place,
                product.rank,
                product.orders
            ])
            if product.shop == shopname:
                format = {'repeatCell': {
                    'range': {
                        'sheetId': 0,
                        'startRowIndex': i + 1,
                        'startColumnIndex': 0,
                        'endColumnIndex': 6,
                        'endRowIndex': i + 2,
                    },
                    'cell': {
                        'userEnteredFormat': {
                            'backgroundColor': {
                                'green': 1,
                                'red': 0.9,
                                'blue': 0.9,
                            },
                        },
                    },
                    'fields': 'userEnteredFormat(backgroundColor)'
                }}
                requests.get('requests').append(format)
            else:
                format = {'repeatCell': {
                    'range': {
                        'sheetId': 0,
                        'startRowIndex': i + 1,
                        'startColumnIndex': 0,
                        'endColumnIndex': 6,
                        'endRowIndex': i + 2,
                    },
                    'cell': {
                        'userEnteredFormat': {
                            'backgroundColor': {
                                'green': 1,
                                'red': 1,
                                'blue': 1,
                            },
                        },
                    },
                    'fields': 'userEnteredFormat(backgroundColor)'
                }}
                requests.get('requests').append(format)
        return body, requests

    @staticmethod
    def __header_generate(table: str) -> tuple[dict, dict]:
        result = {
            "valueInputOption": 'USER_ENTERED',
            "data": [
                {
                    "range": table,
                    "values": [
                        ["Ссылка", "Магазин", "Название товара", "Место выдачи", "Рейтинг", "Количество заказов"]
                    ]
                }
            ],
        }
        requests = {
            'requests': [
                {'repeatCell': {
                    'range': {
                        'sheetId': 0,
                        'startRowIndex': 0,
                        'startColumnIndex': 0,
                        'endColumnIndex': 6,
                        'endRowIndex': 1,
                    },
                    'cell': {
                        'userEnteredFormat': {
                            'backgroundColor': {
                                'green': 0.35,
                                'red': 0.35,
                                'blue': 0.85,
                            },
                        },
                    },
                    'fields': 'userEnteredFormat(backgroundColor)',
                }},
            ]
        }
        return result, requests
