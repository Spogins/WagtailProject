"""Core wagtail hooks module."""

from django.templatetags.static import static
from wagtail import hooks


@hooks.register("get_avatar_url")
def get_profile_avatar(user, size):
    """Get static profile avatar URL."""
    return static("img/logo.png")


@hooks.register("construct_main_menu")
def hide_help_menu_item(request, menu_items):
    """Hide 'Help' menu item."""
    menu_items[:] = [item for item in menu_items if item.name != "help"]


@hooks.register("construct_reports_menu")
def register_reports(request, report_items):
    """Hide unnecessary reports."""
    report_items[:] = [
        item
        for item in report_items
        if item.name not in ["locked-pages", "page-types-usage"]
    ]
