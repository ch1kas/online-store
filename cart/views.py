from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from products.models import Product

from orders.permissions import IsOwner
from .cart import Cart
from .serializers import CartAddProductSerializer, CardProductDetailSerializer

@permission_classes(IsAuthenticated)
@api_view(['POST'])
def cart_add(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)

    if not product:
        raise ValidationError
    serializer = CartAddProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        cd = serializer.data
        cart.add(product=product,
                 id=product.id,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return Response({'status': 'Successfully Created', 'code': 201})


@permission_classes(IsAuthenticated)
@api_view(['POST'])
def cart_remove(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product)
    return Response({'status': 'Successfully removed', 'code': 200})


# @permission_classes(IsOwner)
@csrf_exempt
@api_view(['GET'])
def cart_detail(request):
    cart = Cart(request)
    serializer = CardProductDetailSerializer(cart, many=True)
    return Response(serializer.data)