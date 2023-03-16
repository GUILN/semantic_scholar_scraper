"""
models to describe v1 resources
"""


from typing import List


class Paper:
    """
    semantic scholars representation of paper resource
    """

    def __init__(
        self,
        title: str,
        url: str = None,
        abstract: str = None,
        citation_count: int = None,
        citation_styles: str = None,
        venue: str = None,
        year: int = None,
        authors: List[str] = None,
    ):
        self._title = title
        self._authors = authors
        self._url = url
        self._abstract = abstract
        self._citation_count = citation_count
        self._citation_styles = citation_styles
        self._venue = venue
        self.year = year

    def __dict__(self):
        return {
            "title": self._title,
            "authors": self._authors,
            "url": self._url,
            "abstract": self._abstract,
            "citation_count": self._citation_count,
            "citation_styles": self._citation_styles,
            "venue": self._venue,
            "year": self.year,
        }
