from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ListApiProduct.as_view()),
    path('products/<int:pk>/', DetailApiProduct.as_view()),
    path('products/create/', CreateApiProduct.as_view()),
    path('products/update/<int:pk>/', UpdateApiProduct.as_view()),
    path('products/delete/<int:pk>/', DeleteApiProduct.as_view()),
]