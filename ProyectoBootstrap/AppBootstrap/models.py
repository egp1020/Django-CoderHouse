from django.db import models

# Create your models here.

class Libro(models.Model):
    nombre=models.CharField(max_length=50)
    autor=models.CharField(max_length=70)
    fecha_publicacion=models.DateField(null=True)