from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', ListApiCategory.as_view()),
    path('categories/<int:pk>/', DetailApiCategory.as_view()),
    path('categories/create/', CreateApiCategory.as_view()),
    path('categories/update/<int:pk>/', UpdateApiCategory.as_view()),
    path('categories/delete/<int:pk>/', DeleteApiCategory.as_view()),
]