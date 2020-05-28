from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
import datetime
from proyectoferreteria.apps.gestionadmin.models import Marca, Categoria, Proveedor, Producto, Factura
from proyectoferreteria.apps.gestionadmin.formularios.marca_form import MarcaForm
from proyectoferreteria.apps.gestionadmin.formularios.categoria_form import CategoriaForm
from proyectoferreteria.apps.gestionadmin.formularios.proveedor_form import ProveedorForm
from proyectoferreteria.apps.gestionadmin.formularios.producto_form import ProductoForm
from proyectoferreteria.apps.gestionadmin.formularios.factura_form import FacturaForm

from django.urls import reverse
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


def dash_index(request):
    return render(request,'gestionadmin/dashboard.html')



def vista_principal(request):
    return render(request,'base/baseprincipal.html')


######### Marca ###########
def marca_index(request):
    listaE = Marca.objects.all()
    contexto = {'lista': listaE}
    return render(request, 'gestionadmin/indexmarca.html', contexto)

    
def marca_nueva(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Marca_index')
    else:
        form = MarcaForm()
    return render(request, 'gestionadmin/formmarca.html', {'form':form})

def marca_edit(request, id_exp):
    exp = Marca.objects.get(idMarca=id_exp)
    if request.method == 'GET':
        
        form = MarcaForm(instance=exp)

    else:
        form = MarcaForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
        return redirect('Marca_index') 
    return render(request, 'gestionadmin/formmarca.html', {'form':form})

def marca_delete(request, id_exp):
    exp = Marca.objects.get(idMarca=id_exp)
    if request.method == 'POST':
        exp.delete()
        return redirect('Marca_index') 
    return render(request, 'gestionadmin/formmarca.html', {'form':exp})    

######### Categoría ###########
def categoria_index(request):
    listaE = Categoria.objects.all()
    contexto = {'lista': listaE}
    return render(request, 'gestionadmin/indexcategoria.html', contexto)

    
def categoria_nueva(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Categoria_index') 
    else:
        form = CategoriaForm()
    return render(request, 'gestionadmin/formcategoria.html', {'form':form})

def categoria_edit(request, id_exp):
    exp = Categoria.objects.get(Id_Categoria=id_exp)
    if request.method == 'GET':
        
        form = CategoriaForm(instance=exp)
    else:
        form = CategoriaForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
        return redirect('Categoria_index') 
    return render(request, 'gestionadmin/formcategoria.html', {'form':form})

def categoria_delete(request, id_exp):
    exp = Categoria.objects.get(Id_Categoria=id_exp)
    if request.method == 'POST':
        exp.delete()
        return redirect('Categoria_index') 
    return render(request, 'gestionadmin/formcategoria.html', {'form':exp})    


######### FACTURA ###########
def factura_index(request):
    listaE = Factura.objects.all()
    contexto = {'lista': listaE}
    return render(request, 'gestionadmin/indexfactura.html', contexto)

    
def factura_nueva(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            
            form.save()
        return redirect('Factura_index') 
    else:
        form = FacturaForm()
    return render(request, 'gestionadmin/formfactura.html', {'form':form})

def factura_edit(request, id_exp):
    exp = Factura.objects.get(Id_Factura=id_exp)
    if request.method == 'GET':
        
        form = FacturaForm(instance=exp)
    else:
        form = FacturaForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
        return redirect('Factura_index') 
    return render(request, 'gestionadmin/formfactura.html', {'form':form})

def factura_delete(request, id_exp):
    exp = Factura.objects.get(Id_Factura=id_exp)
    if request.method == 'POST':
        exp.delete()
        return redirect('Factura_index') 
    return render(request, 'gestionadmin/formfactura.html', {'form':exp})    




######### Proveedor ###########
def proveedor_index(request):
    listaE = Proveedor.objects.all()
    contexto = {'lista': listaE}
    return render(request, 'gestionadmin/indexproveedor.html', contexto)

    
def proveedor_nueva(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Proveedor_index') 
    else:
        form = ProveedorForm()
    return render(request, 'gestionadmin/formproveedor.html', {'form':form})

def proveedor_edit(request, id_exp):
    exp = Proveedor.objects.get(Id_Proveedor=id_exp)
    if request.method == 'GET':
        
        form = ProveedorForm(instance=exp)
    else:
        form = ProveedorForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            return redirect('Proveedor_index')
        else:
            return render(request, 'gestionadmin/formproveedor.html', {'form':form}) 
    return render(request, 'gestionadmin/formproveedor.html', {'form':form})

def proveedor_delete(request, id_exp):
    exp = Proveedor.objects.get(Id_Proveedor=id_exp)
    if request.method == 'POST':
        exp.delete()
        return redirect('Proveedor_index') 
    return render(request, 'gestionadmin/formproveedor.html', {'form':exp})    


######### Producto ###########
def producto_index(request):
    listaE = Producto.objects.all()
    contexto = {'lista': listaE}
    return render(request, 'gestionadmin/indexproducto.html', contexto)

    
def producto_nueva(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Producto_index') 
    else:
        form = ProductoForm()
    return render(request, 'gestionadmin/formproducto.html', {'form':form})

def producto_edit(request, id_exp):
    exp = Producto.objects.get(Id_Producto=id_exp)
    if request.method == 'GET':
        
        form = ProductoForm(instance=exp)
    else:
        form = ProductoForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
        return redirect('Producto_index') 
    return render(request, 'gestionadmin/formproducto.html', {'form':form})

def producto_delete(request, id_exp):
    exp = Producto.objects.get(Id_Producto=id_exp)
    if request.method == 'POST':
        exp.delete()
        return redirect('Producto_index') 
    return render(request, 'gestionadmin/formproducto.html', {'form':exp}) 

