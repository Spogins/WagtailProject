# -*- coding: utf-8 -*-
"""
Home app configuration.
"""

from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Home app configuration.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "src.blog"
