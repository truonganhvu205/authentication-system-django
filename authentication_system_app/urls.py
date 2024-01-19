from django.urls import path
from .views import home, login_account, logout_account, register_account
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    
    path('account/login/', login_account, name='login'),
    path('account/logout/', logout_account, name='logout'),
    path('account/register/', register_account, name='register'),
    path('account/reset-password/', 
         auth_views.PasswordChangeView.as_view(template_name='reset_password.html'), 
         name='reset_password'),
]