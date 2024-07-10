from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'title']

# class MenuItemSerializer(serializers.ModelSerializer):
#     price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
#     category = CategorySerializer()
#     class Meta:
#         model = MenuItem
#         fields = ['id','title','price','inventory','category','category_id']

#     def calculate_tax(self, product:MenuItem):
#         return product.price * Decimal(1.1)


class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']

class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory','category','category_id']