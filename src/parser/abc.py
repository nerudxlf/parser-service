from src.schemes.product import ProductSchema


class IParser:
    async def run(self, key_word: str) -> list[ProductSchema]:
        raise NotImplementedError()


class AParser:
    def __call__(self):
        return self
