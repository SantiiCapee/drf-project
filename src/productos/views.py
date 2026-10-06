from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Articulo, Categoria
from .serializers import ArticuloSerializer, CategoriaSerializer


class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Permite GET (acceso libre para cualquier usuario), bloquea automáticamente POST, PUT, DELETE y sale 405 Method Not Allowed
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [AllowAny]


class ArticuloViewSet(viewsets.ModelViewSet):
    """
    CRUD completo: GET, POST, PUT, DELETE, permisos: Cualquiera puede ver, pero se requiere Token JWT para crear, editar o borrar
    """
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Endpoint: /api/articulos/recientes/ 
    @action(detail=False, methods=['get'])
    def recientes(self, request):
        ultimos = Articulo.objects.order_by('-timestamp')[:5]
        serializer = self.get_serializer(ultimos, many=True)
        return Response(serializer.data)