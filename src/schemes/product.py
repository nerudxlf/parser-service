import pydantic as _pydantic


class ProductSchema(_pydantic.BaseModel):
    link: str
    shop: str
    name: str
    place: int
    rank: float
    orders: int

    def __key(self):
        return self.name

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, ProductSchema):
            return self.__key() == other.__key()
        return NotImplemented()
