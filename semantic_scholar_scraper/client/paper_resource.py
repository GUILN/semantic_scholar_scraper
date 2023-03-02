"""
PaperResource

defines the interaction with paper rest api resource
"""


from os import path
from typing import List
import httpx

from semantic_scholar_scraper.client.models import Paper


class PaperResource:
    """
    PaperResource

    defines the interaction with paper rest api resource

    params:
        client: httpx async client reference
        client: base url
    """

    def __init__(
        self,
        client: httpx.AsyncClient,
        base_url: str,
    ):
        self._client = client
        self._base_url = base_url

    async def search_paper(self, search_terms: str) -> List[Paper]:
        """
        search_paper
        runs paper search

        params:
            search_terms
        """
        resource_url = path.join(self._base_url, "paper", "search")
        print(resource_url)
        api_formatted_search_terms = "+".join(search_terms.split(" "))
        query_params = {
            "query": api_formatted_search_terms,
            "limit": 50,
            "fields": "title,authors",
        }
        result = await self._client.get(resource_url, params=query_params)

        print(result.text)

        return None
