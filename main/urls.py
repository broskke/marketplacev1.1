from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('account.urls')),
    path('api/v1/category/', include('category.urls')),
    path('api/v1/posts/', include('post.urls')),
    path('api/v1/comments/', include('comment.urls')),
    path('api/v1/orders/', include('orders.urls')),

]

