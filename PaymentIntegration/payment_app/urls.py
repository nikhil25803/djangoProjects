from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='homepage'),
    path('payment/success', views.payment_status, name='payment-status'),
]