# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
#
# from django.http import Http404
#
# from .models import Favorite
# from .serializers import FavoriteSerializer
# from products.models import Product
# from products.serializers import ProductSerializer



# @api_view(['POST'])
# def add_to_favorite(request):
#     # if not Favorite.objects.all().favorite_prod.id == pk:
#     print(request.data)
#     print(request.user)
#
#     prod = Product.objects.get(id=request.data['product'])
#     serializer = FavoriteSerializer(data=prod)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(user=request.user, product=prod)
#         print(serializer)
#
#     return Response({'status': 'Product added to favorites', 'code': 201})

# class FavoriteListView(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             raise Http404
#
#     def post(self, request, format=None):
#         print(request.user)
#         prod = self.get_object(pk=request.data['product'])
#         request.data['product'] = prod
#         serializer = FavoriteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user, product=prod)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def favorites_detail(request):
#     fav = Favorite.objects.all(user=request.user)
#     prod_serializer = ProductSerializer(fav)
#     return Response(prod_serializer.data)
