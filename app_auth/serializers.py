from rest_framework import serializers
from .models import AuthAssignment, AuthItem

class AuthItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthItem
        fields =('__all__')


class AuthAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthAssignment
        fields = ('__all__')
