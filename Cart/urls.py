from django.urls import path
from .views import ProductListCreateView, ProductDetailView, CartItemListCreateView, CartItemDetailView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart-items/', CartItemListCreateView.as_view(), name='cartitem-list-create'),
    path('cart-items/<int:pk>/', CartItemDetailView.as_view(), name='cartitem-detail'),
]
