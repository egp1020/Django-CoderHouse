from django import forms

class FormPerro(forms.Form):
    nombre = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_creacion = forms.DateField(required=False)
    
class BusquedaPerro(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)