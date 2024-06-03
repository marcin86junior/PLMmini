from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework_api_key.permissions import HasAPIKey
from .models import Product
from .serializers import ProductSerializer
from .serializers import (
    UserSerializer,
)
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action


class ProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['category']

    # Ustawienie uprawnień - IsAuthenticated (dla zalogowanych) lub HasAPIKey (dla klucza API)
    def get_permissions(self):
        if self.request.user.is_authenticated:
            return [IsAuthenticated()]
        else:
            return [HasAPIKey()]
    
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except:
            return Response({"error": "Nie można usunąć produktu"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": "Produkt został pomyślnie usunięty"}, status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]  # Domyślne uprawnienia

    permission_classes_by_action = {
        'register': [AllowAny],
        'login': [AllowAny],
        'logout': [IsAuthenticated],
        'current_user': [IsAuthenticated],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    @action(detail=False, methods=["post"])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registration successful"})
        else:
            return Response(serializer.errors, status=400)

    @action(detail=False, methods=["post"])
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response({"message": "Login successful"})
        else:
            return Response({"error": "Invalid credentials"}, status=400)

    @action(detail=False, methods=["post"])
    def logout(self, request):
        logout(request)
        return Response({"message": "Logout successful"})

    @action(detail=False, methods=["get"])
    def current_user(self, request):
        if request.user.is_authenticated:
            serializer = self.get_serializer(request.user)
            return Response(serializer.data)
        else:
            return Response({"error": "Not logged in"}, status=400)
