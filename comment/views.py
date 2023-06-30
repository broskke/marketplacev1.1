from rest_framework import viewsets, generics
from .models import Comment
from .serializers import CommentSerializer
from products import permissions


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetailView(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAuthorOrAdminOrCommentOwner(), ]
        return [permissions.AllowAny(), ]