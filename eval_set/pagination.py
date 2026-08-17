"""Pagination helpers for the eval set."""

from __future__ import annotations


def paginate(items: list[object], page: int, limit: int) -> list[object]:
    """Return a 1-indexed page of items.

    Page 1 returns the first ``limit`` items, page 2 returns the next
    ``limit`` items, and so on.
    """
    start = page * limit
    end = start + limit
    return items[start:end]


def page_count(items: list[object], limit: int) -> int:
    if limit <= 0:
        raise ValueError("limit must be positive")
    return (len(items) + limit - 1) // limit
