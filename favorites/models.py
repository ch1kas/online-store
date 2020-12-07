# from django.contrib.auth import get_user_model
# from django.db import models
#
# from products.models import Product
#
# User = get_user_model()
#
# class Favorite(models.Model):
#     user = models.OneToOneField(User, related_name='favorites', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, related_name='favorite_prod', on_delete=models.CASCADE, default=None)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
