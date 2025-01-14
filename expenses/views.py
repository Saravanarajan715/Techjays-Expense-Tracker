from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Expense
from django.db.models import Sum, Q
from django.db.models.functions import TruncMonth, TruncDay
from django.utils import timezone
from django.core.paginator import Paginator
import csv
from django.http import HttpResponse
from .forms import CustomUserCreationForm
import json
from datetime import datetime


def home(request):
    return render(request, 'home.html', {'show_navbar': False})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your account has been created! Please log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form, 'show_navbar': False})


def login_view(request):
    return render(request, 'login.html', {'show_navbar': False})


@login_required
def dashboard(request):
    current_month = timezone.now().strftime("%B %Y")
    current_month_expenses = Expense.objects.filter(user=request.user, date__month=timezone.now().month, date__year=timezone.now().year)
    total_expenses = current_month_expenses.aggregate(total=Sum('amount'))['total'] or 0
    recent_expenses = current_month_expenses.order_by('-date')[:5]

    context = {
        'current_month': current_month,
        'total_expenses': total_expenses,
        'recent_expenses': recent_expenses,
        'show_navbar': True  
    }
    return render(request, 'dashboard.html', context)


@login_required
def add_expense(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        date = request.POST.get('date', timezone.now())  
        category = request.POST.get('category')

        if description and amount and category:
            Expense.objects.create(
                user=request.user,
                description=description,
                amount=amount,
                date=date,
                category=category
            )
            messages.success(request, 'Expense added successfully!')
            return redirect('manage_expenses')
        else:
            messages.error(request, 'Please fill in all fields.')

    return render(request, 'add_expense.html', {'show_navbar': True})


@login_required
def manage_expenses(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0
    return render(request, 'manage_expenses.html', {'expenses': expenses, 'total_expenses': total_expenses, 'show_navbar': True})


@login_required
def expense_history(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    
    
    paginator = Paginator(expenses, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'expense_history.html', {
        'page_obj': page_obj,  
        'show_navbar': True  
    })


@login_required
def edit_expense(request, id):
    expense = Expense.objects.get(id=id, user=request.user)
    if request.method == 'POST':
        expense.description = request.POST.get('description')
        expense.amount = request.POST.get('amount')
        expense.date = request.POST.get('date')
        expense.category = request.POST.get('category')
        if expense.description and expense.amount and expense.date and expense.category:
            expense.save()
            messages.success(request, 'Expense updated successfully!')
            return redirect('expense_history')
        else:
            messages.error(request, 'Please fill in all fields.')

    return render(request, 'edit_expense.html', {'expense': expense, 'show_navbar': True})


@login_required
def delete_expense(request, id):
    expense = Expense.objects.get(id=id, user=request.user)
    expense.delete()
    messages.success(request, 'Expense deleted successfully!')
    return redirect('expense_history')


@login_required
def reports(request):
    current_year = datetime.now().year
    current_month = datetime.now().month

    
    monthly_expenses = Expense.objects.filter(user=request.user, date__year=current_year).annotate(month=TruncMonth('date')).values('month').annotate(total=Sum('amount')).order_by('month')
    months = [expense['month'].strftime('%B') for expense in monthly_expenses]
    expenses_by_month = [float(expense['total']) for expense in monthly_expenses]

    
    daily_expenses = Expense.objects.filter(user=request.user, date__year=current_year, date__month=current_month).annotate(day=TruncDay('date')).values('day').annotate(total=Sum('amount')).order_by('day')
    days = [expense['day'].strftime('%d-%B') for expense in daily_expenses]
    expenses_by_day = [float(expense['total']) for expense in daily_expenses]

   
    category_expenses = Expense.objects.filter(user=request.user, date__year=current_year).values('category').annotate(total=Sum('amount'))
    categories = [item['category'] for item in category_expenses]
    expenses_by_category = [float(item['total']) for item in category_expenses]

    context = {
        'months_json': json.dumps(months),
        'expenses_by_month_json': json.dumps(expenses_by_month),
        'days_json': json.dumps(days),
        'expenses_by_day_json': json.dumps(expenses_by_day),
        'categories_json': json.dumps(categories),  
        'expenses_by_category_json': json.dumps(expenses_by_category),  
        'show_navbar': True
    }
    return render(request, 'reports.html', context)


@login_required
def download_csv(request):
    expenses = Expense.objects.filter(user=request.user)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="expenses.csv"'

    writer = csv.writer(response)
    writer.writerow(['Description', 'Amount', 'Category', 'Date'])
    for expense in expenses:
        writer.writerow([expense.description, expense.amount, expense.category, expense.date])
    return response
