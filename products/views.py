from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status


from django.db.models import Q

from .models import Product
from .serializers import ProductSerializer


class MyPaginationClass(PageNumberPagination):
    page_size = 3

'''
Custom pagination
'''

    # def get_paginated_response(self, data):
    #     for i in range(self.page_size):
    #         description = data[i]['description']
    #         if len(description) > 20:
    #             data[i]['description'] = description[:20] + '...'
    #     return super().get_paginated_response(data=data)


class ListApiProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny, ]
    pagination_class = MyPaginationClass

    '''
    List of products created with generic views
    '''

    def get_queryset(self):
        title = self.request.query_params.get('title')
        price = self.request.query_params.get('price')
        queryset = super().get_queryset()
        # print(queryset)
        '''
        Search with keyword (lookup fields: title and description )
        '''
        if title:
            queryset = queryset.filter(Q(title__icontains=title) | Q(description__icontains=title))
            # print("Hello")
        '''
        Filtering with price range
        '''
        if price:
            price_from, price_to = price.split('-')
            queryset = queryset.filter(price__gte=price_from, price__lte=price_to)
        return queryset


class DetailApiProduct(generics.RetrieveAPIView):
    '''
        Rroduct details created with generic views. Anyone can surf and see them.
        '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

class CreateApiProduct(generics.CreateAPIView):
    '''
    Creating products with generic views. Only admin is allowed to do so.
    '''

    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser, ]

class UpdateApiProduct(generics.UpdateAPIView):
    '''
        Updating products with generic views. Only admin is allowed to do so.
    '''

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser, ]

class DeleteApiProduct(generics.DestroyAPIView):
    '''
        Deleting products with generic views. Only admin is allowed to do so.
    '''

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser, ]