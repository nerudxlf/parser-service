from fastapi import HTTPException, status

from src.parser.json.abc import IPageParser


class PageParser(IPageParser):
    def ids(self, data: dict):
        if data.get('errors'):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=data.get("errors")[0].get("message"))
        items = data.get('data').get('makeSearch').get('items')
        for item in items:
            yield item.get('catalogCard').get('productId')

    def pages(self, data: dict) -> int:
        if data.get('errors'):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=data.get("errors")[0].get("message"))
        return data.get('data').get('makeSearch').get('total')
