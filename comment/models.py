# from django.db import models
#
# from post.models import Post
# from django.conf import settings
#
#
# class Comment(models.Model):
#     owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец')
#     post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, verbose_name='Пост')
#     body = models.TextField(max_length=500, verbose_name='Текст комментария')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#
#     def __str__(self):
#         return f'{self.owner} -> {self.post}'
