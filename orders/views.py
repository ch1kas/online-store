from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from .models import Order, OrderItem
from .serializers import OrderCreateSerializer, OrderDetailSerializer, OrderHistorySerializer
from cart.cart import Cart
from .tasks import order_created

User = get_user_model()

'''
Function based view for creating an order. Only those authorized can create products.
'''
@api_view(['POST'])
def order_create(request):
    cart = Cart(request)
    serializer = OrderCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        order = serializer.save(owner=request.user)
        '''
        Saving items in cart as OrderItems if they are valid.
        '''
        for item in cart:
            # print(item)
            id_prod = item['prod_id']
            product = Product.objects.get(pk=id_prod)
            OrderItem.objects.create(order=order,
                                     product=product,
                                     price=item['price'],
                                     quantity=item['quantity'])
        # cleaning cart
        cart.clear()
        # order is created with celery async and confirmation email is sent.
        order_created.delay(order.id)
        # order_paid = Order.objects.get(order.id)
        # order_paid.paid = True
        return Response({'status': 'Your order was successfully placed', 'code': 201})


@api_view(['GET'])
def order_detail(request, order_id):
    '''
    function based view to see order details. Only owner is allowed to see hist order detail.
    '''

    order_ = Order.objects.get(id=order_id)

    print(request.user)
    order = Order.objects.filter(owner=request.user)
    if order_ in order:

        order_serializer = OrderDetailSerializer(instance=order_)
        return Response(order_serializer.data)
    return Response({'status': "Not your order! Can't view order details!"})

@api_view(['GET'])
def order_history(request):
    '''
        function based view to see order history. Only owner is allowed to see hist order history.
    '''

    print(request.user)
    order = Order.objects.filter(owner=request.user)
    print(order)
    var = {}
    for i in range(len(order)):
        order_history = OrderHistorySerializer(instance=order[i])
        var[i] = order_history.data
    return Response(var)


