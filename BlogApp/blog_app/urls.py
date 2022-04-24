from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='homepage'),
    path('createpost/', views.post_create, name='post-create'),
]