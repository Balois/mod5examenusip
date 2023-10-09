from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"grupos", views.GrupoViewSet)
#router.register(r"materiales", views.MaterialViewset)
router.register(r"Ventas", views.VentaViewSet)

urlpatterns = [
     path('contacto/<str:nombre>', views.contacto, name='contacto'),
     path('grupos/', views.grupo, name='grupos'),
     path('materiales/', views.materialFormView, name='materiales'),
     path('', views.index, name='index'),
     path('', include(router.urls))
 
]