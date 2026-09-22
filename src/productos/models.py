from django.db import models



class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    nombre = models.CharField(max_length=150)
    precio = models.IntegerField()
    stock = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name="articulos")

    def __str__(self):
        return self.nombre