from django.urls import path
from . import views

urlpatterns = [
    path('category', views.CategoryView.as_view()),
    path('category/<int:pk>', views.SingleCategoryView.as_view()),
    path('menuitem', views.MenuItemView.as_view()),
    path('menuitem/<int:pk>', views.SingleMenuItemView.as_view()),
    path('cart', views.CartView.as_view()),
    path('flushcart', views.FlushCartView.as_view()),
    path('order', views.OrderView.as_view()),
    path('orderitem', views.OrderItemView.as_view()),
    path('orderitem/<int:pk>', views.SingleOrderItemView.as_view()),
]