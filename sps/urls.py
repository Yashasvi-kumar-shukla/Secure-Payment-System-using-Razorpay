from django.urls import path , include
from .views import comfy_payment, payment_status

urlpatterns = [
    path('',comfy_payment,name='comfy-payment'),
    path('payment-status/',payment_status,name='payment-status')
] 
