"""
Models module for the expenses application.

This module defines the data models used in the application, including
the Expense model for tracking user expenses.
"""

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()

class Expense(models.Model):
    """
    Model representing an expense made by a user.

    Attributes:
        user (User): The user who made the expense.
        description (str): Description of the expense.
        amount (Decimal): Amount of the expense.
        date (DateField): Date when the expense was made.
        category (str): Category of the expense.
    """
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transportation', 'Transportation'),
        ('Entertainment', 'Entertainment'),
        ('Healthcare', 'Healthcare'),
        ('Shopping', 'Shopping'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        """Return a string representation of the expense."""
        return f'{self.description} - ${self.amount} ({self.category})'

def month_year(self):
    """Return the month and year of the expense."""
    return f"{self.date.month} {self.date.year}"

def day(self):
    """Return the day of the expense."""
    return f"{self.date.day} {self.date.month} {self.date.year}"  # Example: "5 10 2024"
