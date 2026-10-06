from rest_framework.routers import DefaultRouter
from .views import ArticuloViewSet, CategoriaViewSet

#router por defecto
router = DefaultRouter()

#ViewSets
router.register(r'articulos', ArticuloViewSet, basename='articulo')
router.register(r'categorias', CategoriaViewSet, basename='categoria')