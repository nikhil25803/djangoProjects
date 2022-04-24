# from termios import VINTR
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
   path('register/', views.register_request, name='register-page'),
   path('login/', views.login_request, name='login-page'),
   path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout-page'),
]