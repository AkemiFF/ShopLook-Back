from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'products', CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls')),
]
