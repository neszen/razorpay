from django.urls import path
from . import views
urlpatterns = [
       path("",views.products,name='products'),
       path('create_order/', views.create_order, name='create_order'),
       path('razorpay_webhook/', views.razorpay_webhook, name='razorpay_webhook'),
       path('payment_status/<str:order_id>/', views.payment_status, name='payment_status'),
]
