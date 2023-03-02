import logging
import sys
import click
import httpx

from semantic_scholar_scraper.cli.async_command import async_cmd

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
    url = "https://www.semanticscholar.org/search"
    params = {"q": term, "sort": "relevance"}
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }

    async with httpx.AsyncClient() as client:
        logger.info("firing the request...")
        try:
            response = await client.get(
                url=url,
                headers=headers,
                params=params,
            )
            logger.info("request has been succeeded")
            logger.info(response.text)
            return response.text
        except Exception as ex:
            logger.error(ex)
            raise ex
