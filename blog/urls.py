from django.urls import path, include
from rest_framework import routers
from .views import ArticleViewSet

blog_router = routers.DefaultRouter()
blog_router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('', include(blog_router.urls)),
]