from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ListApiProduct.as_view()),
    path('products/<int:pk>/', DetailApiProduct.as_view()),
]