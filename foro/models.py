from django.db import models
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=50, null=False)
    contrasena = models.CharField(max_length=50, null=False)
    fecha_nacimiento = models.DateField()
    confirmar_pw = models.CharField(max_length=50, null=False, blank=True)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Topic(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    
    titulo = models.CharField(max_length=200)
    sinopsis = models.CharField(max_length=1000)
    director = models.CharField(max_length=200)
    genero = models.ManyToManyField(Genero)
    descargar = models.TextField()

    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.contenido