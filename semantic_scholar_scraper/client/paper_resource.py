"""
PaperResource

defines the interaction with paper rest api resource
"""


import httpx


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

    def search_paper(self, search_terms: str):
        """
        search_paper
        runs paper search

        params:
            search_terms
        """
