from rest_framework import serializers
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)

from .models import Blog, Author, Category

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['AuthorName'] 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class OnlyDateField(serializers.Field):
    def to_representation(self, value):
        return value.date()

class BlogSerializer(TaggitSerializer, serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    author = AuthorSerializer()
    pub_date = OnlyDateField()
    category = CategorySerializer()
    tags = TagListSerializerField()

    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'image', 'post', 'category', 'reading_time', 'pub_date', 'tags']
