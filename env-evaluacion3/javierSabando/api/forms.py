from dataclasses import field, fields
from tkinter import Widget
from django import forms
from .models import JavierSabando
class PersonaForm(forms.ModelForm):
   class Meta:
      model = JavierSabando
      fields = [
         'nombre',
         'apellido',
         'edad',
         'sexo',
         'telefono',
         'direccion',
         ]
      labels = {
         'nombre':'Nombre',
         'apellido':'Apellido',
         'edad':'Edad',
         'sexo':'Sexo',
         'telefono':'Telefono',
         'direccion':'Direccion',
         }
      widgets = {
         'nombre': forms.TextInput(attrs={'class':'form-input-text'}) ,
         'apellido': forms.TextInput(attrs={'class':'form-input-text'}) ,
         'edad': forms.TextInput(attrs={'class':'form-input-text'}) ,
         'sexo': forms.Select(attrs={'class':'form-input-select'}) ,
         'telefono': forms.TextInput(attrs={'class':'form-input-text'}) ,
         'direccion': forms.TextInput(attrs={'class':'form-input-text'}) ,
      }