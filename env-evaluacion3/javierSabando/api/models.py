from django.db import models

# Create your models here.

class JavierSabando(models.Model):
   SEX = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )
   nombre = models.CharField(max_length=50)
   apellido = models.CharField(max_length=50)
   edad = models.IntegerField()
   sexo = models.CharField(max_length=1, choices=SEX)
   telefono = models.IntegerField()
   direccion = models.CharField(max_length=500)


# -Nombre
# -Apellido
# -Edad
# -Sexo
# -Telefono (inventado)
# -Dirección(inventado)