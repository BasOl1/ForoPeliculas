from django.test import TestCase, Client
from django.urls import reverse
from foro.models import Usuario

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.registro_url = reverse('registro')
        self.usuario1 = Usuario.objects.create(
            nombre = 'loco',
            email = 'test@gmail.com',
            contrasena = '123',
            confirmar_pw = '123',
            fecha_nacimiento = '1990-04-12'
        )

    def test_registro_nombre_existe_objeto_no_se_crea(self):
        response = self.client.post(self.registro_url, {'nombreUsuario':'LoCo', 'correoElectronico':'asd@gmail.com','fechaAnno':'1999','fechaMes':'11','fechaDia':'11','contrasena':'asd','confirmContrasena':'asd'})
        user1 = Usuario.objects.get(id=1)
        
        try:
            return print("Hay 2 usuarios creados: "+Usuario.objects.get(email="asd@gmail.com").nombre+" Y "+user1.nombre)
        except Usuario.DoesNotExist:
            return print("Ya existe un usuario con el NOMBRE INGRESADO("+user1.nombre +"). Tu Objeto 2 no ha sido creado.")

    def test_registro_email_existe_objeto_no_se_crea(self):
        response = self.client.post(self.registro_url, {'nombreUsuario':'TesteoEmail', 'correoElectronico':'tEsT@gmail.com','fechaAnno':'1999','fechaMes':'11','fechaDia':'11','contrasena':'asd','confirmContrasena':'asd'})
        user1 = Usuario.objects.get(id=1)
        
        try:
            return print("Hay 2 usuarios creados: "+Usuario.objects.get(nombre="TesteoEmail").email+" Y "+user1.email)
        except Usuario.DoesNotExist:
            return print("Ya existe un usuario con el EMAIL INGRESADO("+user1.email +"). Tu Objeto 2 no ha sido creado.")