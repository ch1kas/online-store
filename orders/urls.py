from django.urls import path

from .views import order_create, order_detail

urlpatterns = [
    path('cart-checkout/', order_create),
    path('detail/<int:order_id>/', order_detail),
]