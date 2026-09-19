"""Common low-level browser operation placeholders."""

from playwright.sync_api import Page


def safe_click(_page: Page, _selector: str) -> None:
    """Click an element when it is safe to do so."""
    # TODO: Implement safe click behavior.
    raise NotImplementedError
