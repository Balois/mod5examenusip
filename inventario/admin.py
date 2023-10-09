from django.contrib import admin
from .models import Grupo
from .models import Material
from .models import Venta
from .models import DetalleVenta
from .models import Comprador
# Register your models here.

admin.site.register(Grupo)
admin.site.register(Material)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Comprador)
