from django.shortcuts import render, redirect
""" from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView """



from .forms import BusquedaMascota, FormMascota
from .models import Mascota
from datetime import datetime


""" class ListarMascotas(ListView):
    model = Mascota
    template_name = 'mascota/listar_mascotas.html'


class CrearMascota(CreateView):
    model = Mascota
    template_name = 'mascota/crear_mascota.html'
    success_url = '/mascotas'
    fields = ['nombre', 'edad', 'fecha_ingreso']


class EditarMascota(UpdateView):
    model = Mascota
    template_name = 'mascota/editar_mascota.html'
    success_url = '/mascotas'
    fields = ['nombre', 'edad', 'fecha_ingreso']


class EliminarMascota(DeleteView):
    model = Mascota
    template_name = 'mascota/eliminar_mascota.html'
    success_url = '/mascotas'


class MostrarMascota(DetailView):
    model = Mascota
    template_name = 'mascota/mostrar_mascota.html'
"""
def una_vista(request):
    return render(request, 'home/index.html')

def crear_mascota(request):
    if request.method == 'POST':
        form = FormMascota(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            mascota = Mascota(
                nombre=data.get('nombre'),
                edad=data.get('edad'),
                fecha_ingreso=data.get('fecha_ingreso') if data.get('fecha_ingreso') else datetime.now()
            )
            mascota.save()
            return redirect('listar_mascotas')
        
        else:
            return render(request, 'mascota/crear_mascota.html', {'form': form})
            
    
    form_mascota = FormMascota()
    
    return render(request, 'mascota/crear_mascota.html', {'form': form_mascota})

def listar_mascotas(request):
    
    nombre_de_busqueda = request.GET.get('nombre')
    
    if nombre_de_busqueda:
        listar_mascotas = Mascota.objects.filter(nombre__icontains=nombre_de_busqueda) 
    else:
        listar_mascotas = Mascota.objects.all()
    
    form = BusquedaMascota()
    return render(request, 'mascota/listar_mascotas.html', {'listar_mascotas': listar_mascotas, 'form': form})
    
def editar_mascota(request, id):
    mascota = Mascota.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormMascota(request.POST)
        if form.is_valid():
            mascota.nombre = form.cleaned_data.get('nombre')
            mascota.edad = form.cleaned_data.get('edad')
            mascota.fecha_ingreso = form.cleaned_data.get('fecha_ingreso')
            mascota.save()
    
            return redirect('listar_mascotas')
        
        else:
            return render(request, 'mascota/editar_mascota.html', {'form': form, 'mascota': mascota})
            
    form_mascota = FormMascota(initial={'nombre': mascota.nombre, 'edad': mascota.edad, 'fecha_ingreso': mascota.fecha_ingreso})
    
    return render(request, 'mascota/editar_mascota.html', {'form': form_mascota, 'mascota': mascota})
        

def eliminar_mascota(request, id):
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    return redirect('listar_mascotas')

def mostrar_mascota(request, id):
    mascota = Mascota.objects.get(id=id)
    return render(request, 'mascota/mostrar_mascota.html', {'mascota': mascota})