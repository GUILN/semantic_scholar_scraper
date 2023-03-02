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
        authors: List[str],
    ):
        self._title = title
        self._authors = authors
