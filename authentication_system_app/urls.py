from django.urls import path
from .views import home, login_account, logout_account, register_account
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    
    path('login/', login_account, name='login'),
    path('logout/', logout_account, name='logout'),
    path('register/', register_account, name='register'),
    
    # Submit email form
    path('reset-password/', 
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'), 
         name='reset_password'),
    
    # Email sent success message
    path('reset-password-sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'), 
         name='password_reset_done'),
    
    # Link to password reset form in email
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'), 
         name='password_reset_confirm'),
    
    # Password successfully changed message
    path('reset-password-complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), 
         name='password_reset_complete'),
]