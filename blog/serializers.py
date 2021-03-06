from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Article
        fields = ('__all__')
        read_only_fields = ('published', 'promoted', 'comments')