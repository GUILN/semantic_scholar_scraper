"""
PaperResource

defines the interaction with paper rest api resource
"""


from os import path
from typing import List
import httpx
from semantic_scholar_scraper.client.errors import HttpClientError

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

    async def search_paper(
        self,
        search_terms: str,
        limit: int = 50,
        fields: str = "title,authors,url,abstract,citationCount,citationStyles,venue,year",
    ) -> List[Paper]:
        """
        search_paper
        runs paper search

        params:
            search_terms => search terms
            limit => limit results per search
            fields => desired fields separated by comma
        """
        resource_url = path.join(self._base_url, "paper", "search")
        query_params = {
            "query": search_terms.strip(),
            "limit": limit,
            "fields": fields,
        }
        try:
            result = await self._client.get(resource_url, params=query_params)
            if result.status_code >= 300:
                if result.status_code == 429:
                    raise HttpClientError(
                        status_code=result.status_code,
                        reason="api throttled the request, too many requests",
                    )
                raise HttpClientError(
                    status_code=result.status_code,
                    reason="error happened during the request",
                )
        except httpx.HTTPError as err:
            raise HttpClientError(reason=f"status_code={str(err)}", client_error=err)

        print(result.text)

        return None
