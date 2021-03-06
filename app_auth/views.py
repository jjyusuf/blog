from django.shortcuts import render
from rest_framework import viewsets
from .models import AuthAssignment, AuthItem
from .serializers import AuthAssignmentSerializer, AuthItemSerializer


class AuthItemViewSet(viewsets.ModelViewSet):
    queryset = AuthItem.objects.all()
    serializer_class = AuthItemSerializer
    

class AuthAssignmentViewSet(viewsets.ModelViewSet):
    queryset = AuthAssignment.objects.all()
    serializer_class = AuthAssignmentSerializer