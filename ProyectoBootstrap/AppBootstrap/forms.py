from socket import fromshare
from django import forms


class FormLibro(forms.Form):
    nombre=forms.CharField(max_length=50)
    autor=forms.CharField(max_length=70)
    fecha_publicacion=forms.DateField(required=False)