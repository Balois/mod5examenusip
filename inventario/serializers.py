from rest_framework import serializers
from .models import Grupo
from .models import Material
from .models import Venta
from .models import DetalleVenta
from .models import Comprador
from .validators import validar_nombre_subject 


class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = "__all__"

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = "__all__"

class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = "__all__"

class CompradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comprador
        fields = "__all__"

class ReporteMaterialesSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    materiales = MaterialSerializer(many=True)

class ContactSerializer(serializers.Serializer):
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=100, validators=[validar_nombre_subject,])
    body = serializers.CharField(max_length=255)