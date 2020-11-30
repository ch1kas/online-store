from rest_framework.decorators import api_view
from rest_framework.response import Response


# from django.contrib.admin.views.decorators import staff_member_required
# from django.shortcuts import get_object_or_404
# from django.shortcuts import render
from products.models import Product
from .models import Order, OrderItem
from .serializers import OrderCreateSerializer, OrderDetailSerializer, OrderItemDetailSerializer
from cart.cart import Cart
from .tasks import order_created


@api_view(['POST'])
def order_create(request):
    cart = Cart(request)
    serializer = OrderCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        order = serializer.save(owner=request.user)
        for item in cart:
            print(item)
            id_prod = item['prod_id']
            product = Product.objects.get(pk=id_prod)
            OrderItem.objects.create(order=order,
                                     product=product,
                                     price=item['price'],
                                     quantity=item['quantity'])
        cart.clear()
        order_created.delay(order.id)
        # order_paid = Order.objects.get(order.id)
        # order_paid.paid = True
        return Response({'status': 'Your order was successfully placed', 'code': 201})


@api_view(['GET'])
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    # order_item = order.items("")
    # order_item_serializer = OrderItemDetailSerializer(order_item)
    order_serializer = OrderDetailSerializer(instance=order)
    return Response(order_serializer.data)