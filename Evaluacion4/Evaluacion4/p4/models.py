from django.db import models

# Create your models here.
class Moneda(models.Model):
    idmoneda = models.IntegerField(primary_key=True, verbose_name='id moneda')
    moneda = models.CharField(max_length=6, verbose_name='moneda')

    def __str__(self):
        return self.moneda

class Proveedor(models.Model):
    numeroID = models.CharField(max_length=12, primary_key=True, verbose_name='ID')
    image = models.ImageField(upload_to = 'media/', null=True, blank=True)
    nombre = models.CharField(max_length=40, verbose_name='nombre')
    telefono = models.CharField(max_length=10, verbose_name='telefono')
    direccion = models.CharField(max_length=100,  verbose_name='direccion')
    email = models.CharField(max_length=40, verbose_name='correo electronico')
    pais = models.CharField(max_length=20, verbose_name='pais')
    contraseña = models.CharField(max_length=8, verbose_name='contraseña')
    tipomoneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)

    def __str__(self):
        return self.numeroID
