from django.shortcuts import render, redirect
from .models import Moneda, Proveedor
from .form import ProveedorForm

# Create your views here.
def index(request):
    return render (request, 'index.html')
def proveedores(request):
    nombre='José Luis'
    proveedor=Proveedor.objects.all()
    return render(request, 'proveedores.html', context={'nom_usuario': nombre, 'datos':proveedor}, 
    )
def crearProveedor(request):
    if request.method=='POST':
        proveedor_form=ProveedorForm(request.POST,request.FILES)
        if proveedor_form.is_valid():
            post = proveedor_form.save(commit=False)
            post.save()
            return redirect('proveedores')
    else:
        proveedor_form=ProveedorForm()
    return render(request, 'p4/form_proveedor.html',{'proveedor_form': proveedor_form})
def modificarProveedor(request,id):
    proveedor = Proveedor.objects.get(numeroID=id)
    datos = {
        'form': ProveedorForm(instance=proveedor)
    }
    if request.method =='POST':
        formulario = ProveedorForm(data=request.POST, instance = proveedor)
        if formulario.is_valid:
            formulario.save()
            return redirect ('proveedores')
            datos['mensaje'] = "Datos modificados correctamente"
    return render(request,'p4/form_mod_proveedor.html', datos)
def eliminarProveedor(request,id):
    proveedor = Proveedor.objects.get(numeroID=id)
    proveedor.delete()
    return redirect(to="proveedores")