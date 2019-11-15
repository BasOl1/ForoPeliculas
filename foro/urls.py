from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('galeria/',views.galeria,name='galeria'),
    path('registro/',views.CrearUsuario,name='registro'),
    path('creada/',views.CrearUsuario,name='creada'),
    #path('usuarios/', views.usuariolist, name='listausuarios')
    path('usuarios/', views.UsuarioListView.as_view(), name='usuarios')
]

from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]