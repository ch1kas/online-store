from django.urls import path
from .views import *

urlpatterns = [
    path('', cart_detail),
    path('add/<str:product_id>/', cart_add),
    path('remove/<str:product_id>/', cart_remove),
]