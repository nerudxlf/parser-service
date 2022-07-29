from transliterate import translit

from src.parser.json.abc import IProductParser, AProductParser


class ProductParser(IProductParser, AProductParser):
    def link(self) -> str:
        title = translit(self.data.get('payload').get('data').get('title'), language_code='ru', reversed=True)
        link = "-".join(title.split()[:3])
        id = self.data.get('payload').get('data').get('id')
        return f"https://kazanexpress.ru/product/{link}-{id}"

    def shop(self) -> str:
        return self.data.get('payload').get('data').get('seller').get('title')

    def name(self) -> str:
        return self.data.get('payload').get('data').get('title')

    def rank(self) -> float:
        return float(self.data.get('payload').get('data').get('rating'))

    def orders(self) -> int:
        return int(self.data.get('payload').get('data').get('ordersAmount'))
