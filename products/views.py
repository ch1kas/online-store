from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics


class ListApiProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DetailApiProduct(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
