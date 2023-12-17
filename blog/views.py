from django.shortcuts import render, HttpResponse
from .models import Blog, Category, Author
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogSerializer, CategorySerializer , AuthorSerializer


@api_view(["GET","POST"])
def Home(request, blog_id = None):
    print(blog_id)
    if request.method == "GET":
        get_id = blog_id
        if get_id is not None:
            query = Blog.objects.get(id = get_id)
            serializer = BlogSerializer(query)
            return Response(serializer.data)
        
        else:
            query = Blog.objects.all()
            serializer = BlogSerializer(query,many = True)
            return Response(serializer.data)
        
    elif request.method == "POST":
        serializer  = BlogSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        

# Tag API.
@api_view(["GET"])
def get_tag_API(request, tag_name=None):
    get_tags = Blog.objects.filter(tags__name__in=[tag_name])
    serializer = BlogSerializer(get_tags, many=True)
    return Response(serializer.data, )


# category  API
@api_view(["GET"])
def category(request):
    if request.method == "GET":
        query = Category.objects.all()
        serializer = CategorySerializer(query, many=True)
        return Response(serializer.data)


# author API / writers API. 
@api_view(["GET"])
def author(request):
    if request.method == "GET":
        query = Author.objects.all()
        serializer = AuthorSerializer(query, many = True)
        return Response(serializer.data)
    

