#!/usr/bin/env python3
"""Utility functions for handling pagination ranges."""


def index_range(page, page_size):
    """
    Calculate the start and end index for a given pagination page.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple of two integers containing the start index (inclusive)
            and the end index (exclusive) for the items on the given page.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
