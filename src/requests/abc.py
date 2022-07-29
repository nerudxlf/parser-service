from httpx import Response


class IRequests:
    @staticmethod
    async def get(url: str, headers: dict) -> Response:
        raise NotImplementedError()

    async def post(self, url: str, headers: dict, json: dict) -> Response:
        raise NotImplementedError()
