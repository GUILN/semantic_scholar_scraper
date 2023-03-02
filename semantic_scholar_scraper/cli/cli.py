import logging
import sys
import click

from semantic_scholar_scraper.cli.async_command import async_cmd
from semantic_scholar_scraper.client.errors import HttpClientError
from semantic_scholar_scraper.client.semantic_scholar_client import (
    SemanticScholarClient,
)

# creating logger
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)


@click.command()
@click.option(
    "--term",
    prompt="please specify an search term",
    help="term to be used in the search",
)
@async_cmd
async def cli(
    term: str,
):
    """
    cli: defines the entry point for the cli tool.
    """
    logger.info(f"searching for {term}...")  # pylint: disable
    await search_by_term(
        term=term,
    )

    logger.info("finished the search")


async def search_by_term(
    term: str,
) -> str:
    """
    search_term:
    Performs the first search for the given term

    params:
        term: string => term to be used in semantic scholar search

    returns:
        html of the page
    """
    semantic_scholar_client = SemanticScholarClient()
    try:
        await semantic_scholar_client.paper_resource.search_paper(search_terms=term)
    except HttpClientError as err:
        logger.error(err.reason)
