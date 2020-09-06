from django.db import models
import decimal

# Create your models here.
class Producto(models.Model):
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.IntegerField()
    user = models.CharField(max_length=15)
    usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "producto"
        verbose_name = "producto"
        verbose_name_plural = "producto"

    def __str__(self):
        return self.descripcion