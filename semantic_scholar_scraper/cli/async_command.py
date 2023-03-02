"""
async_command:
    This module just provides an wrapper function to make click commands awaitables.
"""
import asyncio
import functools as ft


def async_cmd(func: callable) -> callable:
    """
    async_cmd
    Wraps a function into an asynchronous runner

    Params:
        func: callable
            function to be wrapped

    Returns:
        callable
        wrapper function
    """

    @ft.wraps(func)
    def wrapper(*args, **kwargs):
        return asyncio.run(func(*args, **kwargs))

    return wrapper
