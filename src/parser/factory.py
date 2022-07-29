class ParserFactory:
    def __init__(self):
        self._creators = {}

    def register_parser(self, name: str, obj):
        self._creators[name] = obj

    def get_parser(self, name):
        parser = self._creators.get(name)
        if not parser:
            raise ValueError(name)
        return parser()

