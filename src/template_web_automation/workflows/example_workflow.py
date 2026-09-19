"""Example workflow placeholder."""

from playwright.sync_api import Page

from template_web_automation.pages.example_page import ExamplePage


def run_example_workflow(_page: Page) -> None:
    """Run an example browser workflow."""
    page = ExamplePage(_page)
    # TODO: Implement authentication.
    # TODO: Implement downloads and uploads.
    # TODO: Implement business workflow execution.
    page.submit()
