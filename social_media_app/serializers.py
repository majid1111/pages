
from rest_framework import serializers
from .models import Page, Post, Like

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
