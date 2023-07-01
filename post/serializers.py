from django.db import models
from rest_framework import serializers
from category.models import Category
from .models import Post, PostImage, PostRating


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())
    owner = serializers.ReadOnlyField(source='owner.id')
    images = PostImageSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        images = request.FILES.getlist('images')
        post = Post.objects.create(**validated_data)

        for image in images:
            PostImage.objects.create(image=image, post=post)
        return post


class PostListSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_username = serializers.ReadOnlyField(source='category.name')
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'owner', 'owner_username', 'category', 'category_username', 'preview', 'rating')

    @staticmethod
    def get_rating(obj):
        return obj.rating.aggregate(models.Avg('value'))['value__avg']


class PostDetailSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_username = serializers.ReadOnlyField(source='category.name')
    images = PostImageSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    @staticmethod
    def get_rating(obj):
        return obj.rating.aggregate(models.Avg('value'))['value__avg']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostRating
        fields = '__all__'
