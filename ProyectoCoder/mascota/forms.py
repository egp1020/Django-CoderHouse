from django import forms


class FormMascota(forms.Form):
    nombre = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_ingreso = forms.DateField(required=False)


class BusquedaMascota(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)