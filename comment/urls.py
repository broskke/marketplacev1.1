from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet

urlpatterns = [
    path('', views.CommentCreateView.as_view()),
    path('<int:pk>/', views.CommentDetailView.as_view()),
]