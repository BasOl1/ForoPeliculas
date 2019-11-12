from django.contrib import admin

# Register your models here.

from .models import Usuario, Genero, Topic, Comentario

admin.site.register(Usuario)
admin.site.register(Genero)
admin.site.register(Topic)
admin.site.register(Comentario)