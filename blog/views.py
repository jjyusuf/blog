from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
from lib.app_access_policy import AppAccessPolicy

class ArticleAccessPolicy(AppAccessPolicy):
    name = __package__
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": "authenticated",
            "effect": "allow"
        },
        {
            "action": ["publish", "unpublish", "create"],
            "principal": ["group:editor"],
            "effect": "allow",
            "condition": "is_authorised"           
        },
        {
            "action": ["destroy", "update"],
            "principal": ["*"],
            "effect": "allow",
            "condition": "is_author"         
        },
    ]


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (ArticleAccessPolicy,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    @action(detail=True, methods=['GET'])
    def publish(self, request, pk=None):
        item = self.get_object()
        if item:
            item.published = 'Y'
            item.save()
            return Response({'status': 'Article has been Published'})

    @action(methods=['GET'], detail=True)
    def unpublish(self, request, *args, **kwargs):
        item = self.get_object()
        if item:
            item.published = 'N'
            item.save()
            return Response({'status': 'Article has been UnPublished'})
