"""Define URL patterns for users"""

from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView

from . import views
app_name = 'users'

urlpatterns = [
    # Login page
    re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
]
