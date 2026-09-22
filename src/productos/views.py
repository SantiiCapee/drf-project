from rest_framework import generics
from .models import Articulo, Categoria
from .serializers import ArticuloSerializer, CategoriaSerializer


class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer



class ArticuloListCreate(generics.ListCreateAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer


class ArticuloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer