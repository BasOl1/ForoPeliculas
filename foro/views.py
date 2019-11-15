from django.shortcuts import render
from .models import Usuario, Topic, Genero, Comentario
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages

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

def CrearUsuario(request):
    if request.method == 'POST':
        if request.POST.get('nombreUsuario') and request.POST.get('correoElectronico') and request.POST.get('contrasena') and request.POST.get('confirmContrasena') and request.POST.get('confirmContrasena') and request.POST.get('fechaDia') and request.POST.get('fechaMes') and request.POST.get('fechaAnno'):

            fecha = request.POST.get('fechaAnno')+"-"+request.POST.get('fechaMes')+"-"+request.POST.get('fechaDia')
            usuario=Usuario()
            usuario.nombre = request.POST.get('nombreUsuario')
            usuario.email = request.POST.get('correoElectronico')
            usuario.contrasena = request.POST.get('contrasena')
            usuario.confirmar_pw = request.POST.get('confirmContrasena')
            usuario.fecha_nacimiento = fecha
            usuario.save()
            
            return render(request, 'creada.html')  
    else:
        context= {'error': 'La cuenta no ha sido creada exitosamente. Por favor ingresa nuevamente los datos'}
        return render(request,'registro.html', context)

class UserListView(generic.ListView):
    model = Usuario