from django.db import models
from category.models import Category


class Product(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.PositiveSmallIntegerField(blank=True, default=0)
    preview = models.ImageField(upload_to='media', blank=True, default='media/default-photo.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.preview}'

    class Meta:
        ordering = ('title', 'body', 'category', )
