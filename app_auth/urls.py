from django.urls import path, include
from rest_framework import routers
from .views import AuthItemViewSet, AuthAssignmentViewSet

auth_router = routers.DefaultRouter()
auth_router.register(r'items', AuthItemViewSet)
auth_router.register(r'assignments', AuthAssignmentViewSet)


urlpatterns = [
    path('', include(auth_router.urls)),
]
