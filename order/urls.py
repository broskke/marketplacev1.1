from django.urls import path, include
from order import views
from order.views import OrderListCreateView, OrderDetailView, ProductListCreateView

urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
]
