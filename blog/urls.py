from django.urls import path, include
from .views import ArticleView

app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/<pk>', ArticleView.as_view()),
]