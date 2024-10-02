from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('history/', views.expense_history, name='expense_history'),  
    path('edit_expense/<int:id>/', views.edit_expense, name='edit_expense'),
    path('delete_expense/<int:id>/', views.delete_expense, name='delete_expense'),
    path('add_expense/', views.add_expense, name='add_expense'),

    
    path('reports/', views.reports, name='reports'),
    path('download_csv/', views.download_csv, name='download_csv'),

    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    
    path('manage_expenses/', views.manage_expenses, name='manage_expenses'),

   
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
