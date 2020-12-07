from django.db import models
from categories.models import Category

import random
import os

def get_filename_extension(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 9999999999)
    name, ext = get_filename_extension(filename)
    final_converted_name = f"{new_filename}{ext}"
    return f"cars/{new_filename}/{final_converted_name}"

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to=upload_image_path, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title