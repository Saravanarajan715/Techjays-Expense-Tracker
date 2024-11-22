"""
Admin module for the expenses app.

This module registers the Expense model with the Django admin site,
defining how expenses should be displayed and managed in the admin interface.
"""

from django.contrib import admin
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Expense objects.
    """

    list_display = ('description', 'amount', 'category', 'date', 'user')
    search_fields = ('description', 'category', 'user__username')
    list_filter = ('category', 'date', 'user')
    date_hierarchy = 'date'
    ordering = ['-date']
    list_per_page = 20
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        """
        Custom action to delete selected expenses.

        This method deletes the selected Expense objects and displays a success
        message in the admin interface.
        """
        queryset.delete()
        self.message_user(request, "Selected expenses have been deleted successfully.")

    delete_selected.short_description = "Delete selected expenses"
