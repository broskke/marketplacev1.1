from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Post, Favorite
from . import serializers
from .permishions import IsAuthorOrAdminOrPostOwner


class StandartResultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    pagination_class = StandartResultPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('owner', 'category')
    search_fields = ('title', 'body')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.PostListSerializer
        elif self.action in ('create', 'update', 'partial_update'):
            return serializers.PostCreateSerializer
        return serializers.PostDetailSerializer

    def get_permissions(self):
        if self.action == 'create':
            return (permissions.IsAdminUser(),)  # Только администратор может создавать посты
        elif self.action == 'destroy':
            return (IsAuthorOrAdminOrPostOwner(),)
        elif self.action in ('update', 'partial_update'):
            return (IsAuthorOrAdminOrPostOwner(),)
        return (permissions.IsAuthenticatedOrReadOnly(),)

    @action(['POST', 'DELETE'], detail=True)
    def favorites(self, request,):
        post = self.get_object()
        user = request.user
        favorite = user.favorites.filter(post=post)

        if request.method == 'POST':
            if user.favorites.filter(post=post).exists():
                return Response({'msg': 'Already in Favorite'}, status=400)
            Favorite.objects.create(owner=user, post=post)
            return Response({'msg': 'Added to Favorite'}, status=201)

        if favorite.exists():
            favorite.delete()
            return Response({'msg': 'Deleted from Favorite'}, status=204)
        return Response({'msg': 'Post not Found in Favorite'}, status=404)
