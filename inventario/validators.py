from django.core.exceptions import ValidationError

def validar_precio(value):
    if value == 0:
       raise ValidationError("No es una opcion permitida")

def validar_nombre_grupo(value):
    if value == '':
        raise ValidationError("No es una opcion permitida")
    
def validar_nombre_comprador(value):
    if value == '':
        raise ValidationError("No es una opcion permitida")

def validar_nombre_subject(value):
    if value == '':
        raise ValidationError("No es una opcion permitida")