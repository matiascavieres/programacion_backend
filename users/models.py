from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Habito(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Código")
    habito = models.CharField(max_length=20, verbose_name="Hábito")
    donde = models.CharField(max_length=20, verbose_name="Dónde")
    cantidad = models.CharField(max_length=20, verbose_name="Cantidad")

    def __str__(self):
        fila = "Hábito: " + self.habito + " - " + "Dónde: " + self.donde + " - " + "Cantidad: " + self.cantidad
        return fila