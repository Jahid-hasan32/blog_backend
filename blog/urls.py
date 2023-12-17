from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:blog_id>/', views.Home, name="home"),
    path('', views.Home, name="home"),
    path('category/', views.category, name="category"),
    path('author/', views.author, name="author"),
    path('tags/<slug:tag_name>/', views.get_tag_API, name="gat_tag_API")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

