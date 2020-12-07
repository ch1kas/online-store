# from rest_framework import serializers
# from .models import Favorite
#
# class FavoriteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Favorite
#         # fields = ('user', 'product')
#         fields = ('product',)

    # def validate(self, attrs):
    #     product = attrs.get('product')
    #     user = attrs.get('user')
    #     if product in  Favorite.objects.get(pk=user).favorite_prod:
    #         raise serializers.ValidationError("Already in favorites!")
    #     return attrs
