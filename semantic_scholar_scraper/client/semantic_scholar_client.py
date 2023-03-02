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
        base_url: str = "https://api.semanticscholar.org/graph/v1",
    ):
        self._client = httpx.AsyncClient()
        self._base_url = base_url
        self._paper_resource = PaperResource(
            base_url=self._base_url, client=self._client
        )

    @property
    def paper_resource(self) -> PaperResource:
        """
        paper_resource
        """
        return self._paper_resource