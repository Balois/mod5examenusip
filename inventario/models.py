from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings
from .validators import validar_precio
from .validators import validar_nombre_grupo 
from .validators import validar_nombre_comprador
# from django.core.validators import EmailValidator 


class Grupo(models.Model):
    nombre = models.CharField(max_length=100, unique=True, validators=[validar_nombre_grupo,]) 

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = [
            ("reporte_cantidad", "Visualizar el reporte de cantidad"),
            ("reporte_detalle", "Reporte detallado de cantidades"),
        ]


class Comprador(models.Model):
    nombre = models.CharField(max_length=100, unique=True, validators=[validar_nombre_comprador,]) 
    nit = models.TextField()
    estado = models.BooleanField(blank=True, default=True)
    def __str__(self):
        return self.nombre

class MaterialUnits(models.TextChoices):
    UNITS = 'u', 'Unidades'
    KG = 'kg', 'Kilogramos'

class Material(models.Model):
    nombre = models.CharField(max_length=100, unique=True) 
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE) 
    precio = models.DecimalField(decimal_places=2, max_digits=10, validators=[validar_precio,])
    unidades = models.CharField(
        max_length=2,
        choices=MaterialUnits.choices,
        default=MaterialUnits.UNITS
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Material - %s" % self.nombre

class EstadoVenta(models.TextChoices):
    NOFACTURADO = 'nofacturado', 'No Facturado'
    FACTURADO = 'facturado', 'Facturado'

class Venta(models.Model):
    fecha = models.DateField()
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE)
    estado = models.CharField(
        max_length=12,
        choices=EstadoVenta.choices,
        default=EstadoVenta.NOFACTURADO
    )

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE) 
    material = models.ForeignKey(Material, on_delete=models.CASCADE) 
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(decimal_places=2, max_digits=10)
