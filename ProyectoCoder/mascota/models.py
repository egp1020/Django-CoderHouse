from django.db import models

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_ingreso = models.DateField(null=True)

    def __str__(self) -> str:
        return f"Soy una nueva mascota llamada {self.nombre}."