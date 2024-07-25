from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from source.accounts.views import login_view, logout_view

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view.as_view(template_name="login.html"), name='login'),
    path('logout/', logout_view.as_view(), name='logout'),
]