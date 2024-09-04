from django.db import models

# Create your models here.
class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    nro_apartamento = models.CharField(max_length=4)
    telefono = models.CharField(max_length=9)
    email= models.CharField(max_length=50)

class Vehiculo(models.Model):
    nom_propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=6)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    color = models.CharField(max_length=10)

class Registro(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_hora_entrada = models.DateTimeField('fecha y hora de entrada')
    fecha_hora_salida = models.DateTimeField('fecha y hora de salida')
    