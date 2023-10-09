from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from django.http import HttpResponse
from .forms import MaterialForm
from .models import Grupo
from .models import Material
from .models import Venta
from .models import DetalleVenta
from .models import Comprador

from .serializers import GrupoSerializer
from .serializers import MaterialSerializer
from .serializers import VentaSerializer
from .serializers import DetalleVentaSerializer
from .serializers import CompradorSerializer

def index(request):
    return HttpResponse("Hola Mundo")

def contacto(request, nombre):
    return HttpResponse(f"Bienvenido {nombre} a la clase de Django")


def grupo(request):
    post_nombre = request.POST.get('nombre')
    if post_nombre:
        q = Grupo(nombre=post_nombre)
        q.save()

    filtro_nombre = request.GET.get("nombre")
    if filtro_nombre:
        grupos = Grupo.objects.filter(nombre__contains=filtro_nombre)
    else:
        grupos = Grupo.objects.all()
    
    return render(request, "grupos.html", {"grupos": grupos})

def materialFormView(request):
    form = MaterialForm()
    material = None
    
    id_material = request.GET.get('id')
    if id_material:
        material = material.objects.get(id=id_material)
        material = get_object_or_404(material, id=id_material)
       #form = MaterialForm(instance=material)

    if request.method == 'POST':
        if material:
            form = MaterialForm(request.POST, instance=material)
        else:
            form = MaterialForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, "form_materiales.html", {"form": form})

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    #permission_classes = [IsUserAlmacen]


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer