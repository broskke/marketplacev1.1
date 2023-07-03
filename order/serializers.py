from rest_framework import serializers
from post.models import Post
from .models import Order
from .models import Order, OrderItem


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    product = PostSerializer()

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), many=True)
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'items']
        fields = ['id', 'user', 'created_at', 'order_items']


