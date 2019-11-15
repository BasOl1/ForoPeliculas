from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('registro/',views.CrearUsuario,name='registro'),
    path('creada/',views.CrearUsuario,name='creada'),
    path('usuarios/', views.UsuarioListView.as_view(), name='usuarios'),
    path('topics/', views.TopicListView.as_view(), name='temas'),
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