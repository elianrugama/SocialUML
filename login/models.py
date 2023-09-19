from django.db import models

# Create your models here.

class Codigo(models.Model):
    codigo = models.CharField(max_length=255)
    usuario = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=255)

    def __str__(self):
        return self.codigo
