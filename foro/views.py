from django.shortcuts import render
from .models import Usuario

# Create your views here.
def index(request):
    "Funcion vista para la pagina inicio del sitio"
    #generar contador de objetos principales
    num_usuarios = Usuario.objects.count()

    #Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_usuarios':num_usuarios},
    )

def galeria(request):
    return render(request,'galeria.html')

def registro(request):
    return render(request,'registro.html')

def creada(request):
    return render(request,'creada.html')