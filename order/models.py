from account.models import CustomUser
from django.db import models

from post.models import Post


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.ForeignKey(Post, related_name='order_items', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='order_post', on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.pk} for {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Post, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.order} - {self.product}"
