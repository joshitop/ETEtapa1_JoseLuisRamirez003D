from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Moneda, Proveedor

class ProveedorForm(forms.ModelForm):
    numeroID = forms.CharField(label='numero id', min_length=9, max_length=12, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su Número de ID',
            'id': 'numero',
            'onkeyup': 'myFunction();'
        }
    ))
    image = forms.ImageField(label='Imagen', widget=forms.ClearableFileInput(
        attrs={
            'class' : 'form-control'
        }
    ))
    nombre = forms.CharField(label='Nombre', min_length=3, max_length=40, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese Nombre',
            'id': 'nombre',
            'onkeyup': 'myFunction();'
        }
    ))
    telefono = forms.IntegerField(label='Teléfono',  widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su Teléfono',
            'id': 'telefono',
            'onkeyup': 'myFunction();'
        }
    ))
    direccion = forms.CharField(label='Dirección', max_length=40, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese Dirección'
        }
    ))
    email = forms.EmailField(label='Correo Electrónico',  widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Correo Electrónico'
        }
    ))
    pais = forms.CharField(label='País',  widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su País',
            'id':'pais',
            'onkeyup': 'myFunction();'
        }
    ))
    contraseña =forms.CharField(label='Contraseña',  widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'contrasena',
            'readonly' : 'readonly'
            
        }
    ))
    tipomoneda = forms.ModelChoiceField(queryset=Moneda.objects.all(),label='Moneda',  widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))
    class Meta:
        model=Proveedor
        fields=['numeroID','image','nombre','telefono','direccion','email','pais','contraseña','tipomoneda']