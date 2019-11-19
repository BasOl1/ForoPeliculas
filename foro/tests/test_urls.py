from django.test import SimpleTestCase
from django.urls import reverse, resolve
from foro.views import index, CrearUsuario, TopicListView, TopicDetailView, TopicCreate, TopicUpdate, TopicDelete

class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)
    def test_registro_url_is_resolved(self):
        url = reverse('registro')
        self.assertEquals(resolve(url).func, CrearUsuario)
    def test_creada_url_is_resolved(self):
        url = reverse('creada')
        self.assertEquals(resolve(url).func, CrearUsuario)
    def test_temas_url_is_resolved(self):
        url = reverse('temas')
        self.assertEquals(resolve(url).func.view_class, TopicListView)
    def test_detalle_temas_url_is_resolved(self):
        url = reverse('detalle-temas', args=['1'])#le pasa como argumento la id del topic 1 para testear
        self.assertEquals(resolve(url).func.view_class, TopicDetailView)
    def test_crear_post_url_is_resolved(self):
        url = reverse('crear-post')
        self.assertEquals(resolve(url).func.view_class, TopicCreate)
    def test_editar_post_url_is_resolved(self):
        url = reverse('editar-post', args=['1'])
        self.assertEquals(resolve(url).func.view_class, TopicUpdate)
    def test_eliminar_post_url_is_resolved(self):
        url = reverse('eliminar-post', args=['1'])
        self.assertEquals(resolve(url).func.view_class, TopicDelete)
