"""
Apps module for the expenses application.

This module defines the configuration for the expenses app.
"""

from django.apps import AppConfig


class ExpensesConfig(AppConfig):
    """
    Configuration class for the Expenses application.

    This class defines the default auto field type and the name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'expenses'
