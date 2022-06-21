from django.contrib import admin
from .models import JavierSabando

# Register your models here.

class Person(admin.ModelAdmin):
   list_display = ('nombre','apellido','edad','sexo','telefono','direccion',)
   list_filter = ('sexo', 'edad')
   pass

admin.site.register(JavierSabando, Person)