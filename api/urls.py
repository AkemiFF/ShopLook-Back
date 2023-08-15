from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'cart', CartViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('v1/', include('rest_framework.urls')),
    path("auth/", include("accounts.urls")),
]
