from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, UserViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r"user_create", UserViewSet, basename="user_create")

urlpatterns = [
    path('', include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]