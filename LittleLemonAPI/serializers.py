from rest_framework import serializers
from .models import Category, MenuItem, Cart, Order, OrderItem
from decimal import Decimal
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['id','title']
        
class MenuItemSerializer(serializers.ModelSerializer):
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ['id','title','price','price_after_tax','featured','category','category_id']
        extra_kwargs = {
            'price':{'min_value':2},
            'inventory':{'min_value':0}
        }
    def calculate_tax(self,product:MenuItem):
        return product.price *Decimal(1.1)

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields = ['id','user','menuitem','quantity','unit_price']
        
    validators=[
        UniqueTogetherValidator(
            queryset=Cart.objects.all(),
            fields=['user','menuitem','quantity']
        )
    ]
    
    extra_kwargs ={
            'quantity':{'min_value':0},
            'unit_price':{'min_value':0}
        }
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields =['id','user','delivery_crew','status','total','date']
    
    validators=[
        UniqueTogetherValidator(
            queryset=Order.objects.all(),
            fields=['user','status']
        )
    ]
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= OrderItem
        fields =['id','order','menuitem','quantity','unit_price']
        extra_kwargs ={
            'quantity':{'min_value':0},
            'unit_price':{'min_value':1}
        }
