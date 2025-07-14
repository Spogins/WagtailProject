# -*- coding: utf-8 -*-
"""Core template tags for project."""

import json
from functools import lru_cache

from django import template

from config import settings
from django.urls import translate_url as django_translate_url

register = template.Library()


@lru_cache
@register.simple_tag
def css_path(key: str):
    """Get css path with hash from manifest.json file."""
    try:
        with open(settings.DJANGO_VITE_MANIFEST_PATH, "r") as file:
            tmp_file = json.load(file)
        value = tmp_file.get(key)
        if value:
            path_with_hash = value.get("file")
        else:
            path_with_hash = key
        return "/static/nodejs/" + path_with_hash
    except FileNotFoundError:
        pass


@register.simple_tag(takes_context=True)
def https_url(context, location=None):
    """
    Create the absolute URI with https protocol regardless of the original request protocol.

    Only forces HTTPS when DEBUG=False.

    Usage:
    {% https_url %}  # Returns current URL with https
    {% https_url '/some/path/' %}  # Returns specific path with https
    """
    request = context.get("request")
    if not request:
        return ""

    uri = request.build_absolute_uri(location)

    if uri.startswith("http://"):
        uri = uri.replace("http://", "https://", 1)

    return uri


@register.simple_tag(takes_context=True)
def translate_url(context, language):
    """
    Get the absolute URL of the current page for a different language.
    """
    return django_translate_url(context["request"].build_absolute_uri(), language)
