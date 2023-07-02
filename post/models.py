from random import randint
from django.db import models
from django.conf import settings
from category.models import Category
# from orders.models import OrderItem


class Post(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, default=0)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.SET_NULL, null=True)
    preview = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # order_items = models.ManyToManyField(OrderItem, related_name='products')

    class Meta:
        ordering = ('title', 'body', 'category', 'preview', 'comments', 'quantity')

    def __str__(self):
        return f"{self.title}: {self.preview}"


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='favorites', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='favorited_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.post.title}'


class PostImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)

    def generate_name(self):
        return 'image' + str(self.id) + str(randint(100000, 999999))

    def save(self, *args, **kwargs):
        self.title = self.generate_name()
        return super(PostImage, self).save(*args, **kwargs)


class PostRating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Пользователь", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name="Пост", on_delete=models.CASCADE, related_name='rating')
    value = models.PositiveIntegerField("Рейтинг")

    def __str__(self):
        return f"{self.user} - {self.post} - {self.value}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

