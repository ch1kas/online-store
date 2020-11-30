from rest_framework import serializers

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductSerializer(serializers.Serializer):
    quantity = serializers.ChoiceField(choices=PRODUCT_QUANTITY_CHOICES, default=1)
    update = serializers.BooleanField(required=False, initial=False)

class CardProductDetailSerializer(serializers.Serializer):
    product = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    quantity = serializers.IntegerField(min_value=1)

