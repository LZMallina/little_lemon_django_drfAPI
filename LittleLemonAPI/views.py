from django.shortcuts import render
from rest_framework import generics
from .serializers import CategorySerializer, MenuItemSerializer, CartSerializer, OrderSerializer, OrderItemSerializer
from .models import Category, MenuItem, Cart, Order, OrderItem
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SingleCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class MenuItemView(generics.ListCreateAPIView):
    throttle_classes =[AnonRateThrottle, UserRateThrottle]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields =['price','title']
    filterset_fields =['price','title']
    search_fields =['title']
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
class FlushCartView(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
class OrderView(generics.ListCreateAPIView):
    if Cart.quantity == 0:
        queryset = Order.objects.all()
        serializer_class = OrderSerializer
    
    def get_permissions(self):
        if(self.request.method == 'GET'):
            return []
        return [IsAuthenticated()]

class OrderItemView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
class SingleOrderItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer