
from django.contrib import admin
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    
    list_display = ('description', 'amount', 'category', 'date', 'user')
    
    
    search_fields = ('description', 'category', 'user__username')
    
    
    list_filter = ('category', 'date', 'user')

    
    date_hierarchy = 'date'

    
    ordering = ['-date']

    
    list_per_page = 20

    
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        #
        queryset.delete()
        self.message_user(request, "Selected expenses have been deleted successfully.")
    delete_selected.short_description = "Delete selected expenses"
