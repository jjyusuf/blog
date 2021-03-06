from django.urls import path
from rest_framework import routers
from .views import AuthItemViewSet, AuthAssignmentViewSet

auth_router = routers.DefaultRouter()
auth_router.register(r'^auth/items', AuthItemViewSet)
auth_router.register(r'^auth/assignments', AuthAssignmentViewSet)

