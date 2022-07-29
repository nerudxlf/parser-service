class AProductParser:
    def __init__(self, data: dict):
        self.data = data


class IProductParser:
    def link(self) -> str:
        raise NotImplementedError()

    def shop(self) -> str:
        raise NotImplementedError()

    def name(self) -> str:
        raise NotImplementedError()

    def rank(self) -> float:
        raise NotImplementedError()

    def orders(self) -> int:
        raise NotImplementedError()


class IPageParser:
    def ids(self, data: dict) -> list[str]:
        raise NotImplementedError()

    def pages(self, data: dict) -> int:
        raise NotImplementedError()
