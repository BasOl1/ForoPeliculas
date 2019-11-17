from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30, null=False,unique=True)
    email = models.EmailField(max_length=50, null=False,unique=True)
    contrasena = models.CharField(max_length=50, null=False)
    confirmar_pw = models.CharField(max_length=50, null=False, blank=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Topic(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200, unique=True)
    anho_estreno = models.IntegerField('Año estreno', validators=[MinValueValidator(1900), MaxValueValidator(2020)], default=0)
    sinopsis = models.TextField(blank=True, null=True)
    director = models.CharField(max_length=200)
    genero = models.ManyToManyField(Genero)
    descargar = models.URLField('Link Descarga',max_length=250,blank=True, null=True)
    portada = models.ImageField(blank=True, null=True,
        upload_to="portadas", default='question_mark.jpg')

    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('detalle-temas', args=[str(self.id)])

class Comentario(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.contenido