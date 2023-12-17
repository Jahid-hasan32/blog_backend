from django.db import models
import uuid 
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

# Create your models here.

class Author(models.Model):
    AuthorName = models.CharField(max_length=100)

    def __str__(self):
        return self.AuthorName


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"


class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='author')
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    post = RichTextUploadingField()  
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category')
    tags = TaggableManager()
    reading_time = models.PositiveIntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)



