from django.urls import path 
from .views import (CategoriaListCreate, CategoriaDetail, ArticuloListCreate, ArticuloDetail
)


urlpatterns = [
    path("categorias/", CategoriaListCreate.as_view(), name="categoria-list-create"),
    path("categorias/<int:pk>/", CategoriaDetail.as_view(), name="categoria-detail"),
    path("articulos/", ArticuloListCreate.as_view(), name="articulo-list-create"),
    path("articulos/<int:pk>/", ArticuloDetail.as_view(), name="articulo-detail"),
]
