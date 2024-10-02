from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Expense(models.Model):
    
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
        return f'{self.description} - ${self.amount} ({self.category})'

    
    def month_year(self):
        return self.date.strftime('%B %Y')

    
    def day(self):
        return self.date.strftime('%d %B')

   
    class Meta:
        ordering = ['-date']
