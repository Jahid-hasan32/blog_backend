from django.contrib import admin
from .models import Author, Blog, Category
# Register your models here.


# class AuthorInline(admin.TabularInline):
#     model = Author
#     extra = 2

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','AuthorName']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','author', 'category']
    search_fields = ['id', 'title']
    # prepopulated_fields = {"slug":["title"]}

    # inlines = [AuthorInline]
    

# class BlogInline(admin.TabularInline):
#     model = Blog
#     extra = 1

# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ['id', 'AuthorName']
#     search_fields = ['id', 'AuthorName']
#     inlines = [BlogInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    
