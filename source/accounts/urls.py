from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from source.accounts.views import login_view, logout_view, RegistrationView

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view.as_view(), name='login'),
    path('logout/', logout_view.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register')
]