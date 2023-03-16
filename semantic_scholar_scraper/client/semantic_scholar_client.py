"""
semantic scholar client to use public semanti scholar api: https://www.semanticscholar.org/product/api
"""

import httpx
from semantic_scholar_scraper.client.paper_resource import PaperResource


class SemanticScholarClient:
    """
    semantic scholar client to use public semantic scholar api: https://www.semanticscholar.org/product/api

    constructor params:
        base_url(optional)
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.semanticscholar.org/graph/v1",
    ):
        self._client: httpx.AsyncClient = None
        self._paper_resource: PaperResource = None
        self._base_url = base_url
        self._api_key = api_key

    async def __aenter__(self):
        self._client = httpx.AsyncClient(
            headers={"x-api-key": self._api_key}, timeout=300
        )
        self._paper_resource = PaperResource(
            base_url=self._base_url, client=self._client
        )
        return self

    async def __aexit__(self, *args):
        await self._client.aclose()

    @property
    def paper_resource(self) -> PaperResource:
        """
        paper_resource
        """
        return self._paper_resource

    async def close(self):
        """
        close

        Releases resources
        """
        await self.__aexit__()
