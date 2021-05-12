from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import authentication, permissions
from lib.app_access_policy import AppAccessPolicy
from .services import create_article, update_article

""" class ArticleAccessPolicy(AppAccessPolicy):
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
    ] """



class ArticleView(APIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        articles = Article.objects.all()
        return Response(ArticleSerializer(articles, many=True).data)


    def post(self, request, format=None):
        article = request.data

        item = ArticleSerializer(data=article)
        if item.is_valid(raise_exception=True):
            article = create_article(**item.data, owner=request.user, published='No', promoted='NO')
        return Response(ArticleSerializer(article,).data)

    def put(self, request, pk):
        saved_article = Article.objects.get(pk=pk)
        data = request.data
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_article = update_article(pk, **serializer.data)

        return Response(serializer.data)

    # @action(detail=True, methods=['GET'])
    # def publish(self, request, pk=None):
    #     item = self.get_object()
    #     if item:
    #         item.published = 'Y'
    #         item.save()
    #         return Response({'status': 'Article has been Published'})

    # @action(methods=['GET'], detail=True)
    # def unpublish(self, request, *args, **kwargs):
    #     item = self.get_object()
    #     if item:
    #         item.published = 'N'
    #         item.save()
    #         return Response({'status': 'Article has been UnPublished'})
