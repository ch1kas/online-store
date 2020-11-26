from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', ListApiCategory.as_view()),
    path('categories/<int:pk>/', DetailApiCategory.as_view()),
]