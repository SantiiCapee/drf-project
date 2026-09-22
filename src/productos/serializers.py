from rest_framework import serializers
from .models import Articulo, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = [
            "id",
            "nombre",
            "descripcion",
        ]
        read_only_fields= ["id"] 


class ArticuloSerializer(serializers.ModelSerializer):
        categoria = CategoriaSerializer(read_only=True)
        categoria_id = serializers.PrimaryKeyRelatedField(
            queryset=Categoria.objects.all(), source="categoria", write_only=True, required=False, allow_null=True)
        class Meta:
            model = Articulo
            fields = [
                "id",
                "nombre",
                "precio",
                "stock",
                "timestamp",
                "categoria",
                "categoria_id"
            ]
            read_only_fields= ["id", "timestamp"]