from .models import Category
from .serializers import CategorySerializer
from rest_framework import generics


class ListApiCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DetailApiCategory(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
