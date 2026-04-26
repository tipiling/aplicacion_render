from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    cedula = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
# Create your models here.
