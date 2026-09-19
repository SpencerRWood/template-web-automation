"""Browser and session lifecycle placeholders."""

from playwright.sync_api import Browser, BrowserContext, Playwright


def create_browser(_playwright: Playwright) -> Browser:
    """Create a browser instance."""
    # TODO: Implement browser initialization.
    raise NotImplementedError


def create_context(_browser: Browser) -> BrowserContext:
    """Create a browser context."""
    # TODO: Implement context creation.
    raise NotImplementedError
