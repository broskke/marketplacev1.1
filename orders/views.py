from rest_framework import generics
from .models import Order, OrderItem
from .serializers import OrderSerializer, PostSerializer
from post.models import Post


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        items_data = self.request.data.get('items', [])
        order = serializer.save(user=self.request.user)

        for item_data in items_data:
            product_id = item_data.get('id')
            quantity = item_data.get('quantity')
            product = Post.objects.get(id=product_id)
            OrderItem.objects.create(order=order, product=product, quantity=quantity)


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
