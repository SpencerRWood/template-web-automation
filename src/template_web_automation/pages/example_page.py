"""Example page interaction placeholders."""

from playwright.sync_api import Page


class ExamplePage:
    """Placeholder page object for one website page."""

    def __init__(self, page: Page) -> None:
        self.page = page

    def submit(self) -> None:
        """Submit the page workflow step."""
        # TODO: Implement page interactions.
        raise NotImplementedError
