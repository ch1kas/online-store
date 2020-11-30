from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer
from products.models import Product


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'address', 'city', 'postal_code']

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description',  'category')



class OrderItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'price', 'product', 'quantity')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product_details'] = ProductDetailSerializer(instance=instance.product).data
        return representation

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'owner', 'full_name', 'email', 'address', 'city',
                  'postal_code', 'created_at', 'updated_at', 'paid')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['order_items'] = OrderItemDetailSerializer(instance=instance.items.all(), many=True).data
        return representation

