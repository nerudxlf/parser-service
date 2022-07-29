from config import qraphql_headers, api_headers
from src.parser.abc import IParser, AParser
from src.parser.json.abc import IPageParser, IProductParser
from src.parser.json.page_parser import PageParser
from src.parser.json.product_parser import ProductParser
from src.requests.requests import Requests
from src.schemes.product import ProductSchema


class JsonParser(IParser, AParser):
    async def run(self, key_word: str) -> list[ProductSchema]:
        result = []
        items: list[str] = []
        requests = Requests()
        page_parser: IPageParser = PageParser()
        req = await requests.post("https://dshop.kznexpress.ru/", qraphql_headers, key_word)
        req = req.json()
        pages = page_parser.pages(req)
        items += page_parser.ids(req)
        total_pages = int(pages / 100)
        for page in range(1, total_pages):
            req = await requests.post("https://dshop.kznexpress.ru/", qraphql_headers, key_word, page)
            req = req.json()
            items += page_parser.ids(req)

        for counter, item in enumerate(items):
            current_product = await requests.get(f"https://api.kazanexpress.ru/api/v2/product/{item}", api_headers)
            if not current_product:
                continue
            current_product = current_product.json()
            product_parser: IProductParser = ProductParser(current_product)
            product: ProductSchema = ProductSchema(
                link=product_parser.link(),
                name=product_parser.name(),
                shop=product_parser.shop(),
                place=counter + 1, rank=product_parser.rank(),
                orders=product_parser.orders()
            )
            result.append(product)
        return result
