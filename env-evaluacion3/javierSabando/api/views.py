import json
from multiprocessing import context
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View, generic
from django.views.decorators.csrf import csrf_exempt
from .models import JavierSabando
from django.shortcuts import redirect

# Create your views here.

def redirect_view(request):
    response = redirect('lista/')
    return response

class listPerson(generic.ListView):
   model = JavierSabando
   template_name = "lista_persona.html"

class JavierSabandoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):

        if(id>0):
            objt = list(JavierSabando.objects.filter(id = id).values())
            if len(objt) > 0:
                per = objt[0]
                datos = {'message':"Succes",'Person':per}
            else:
                datos = {'message':"Person not found..."}
            return JsonResponse(datos)
        if(id == 0):
            objt = list(JavierSabando.objects.values())
            if len(objt) > 0:
                datos = {'message':"Succes",'Persons':objt}
            else:
                datos = {'message':"Persons not found..."}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        JavierSabando.objects.create(nombre=jd['nombre'],apellido=jd['apellido'],edad=jd['edad'],sexo=jd['sexo'],telefono=jd['telefono'],direccion=jd['direccion'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        objtlist = list(JavierSabando.objects.filter(id=id).values())
        if len(objtlist) > 0:
            objt = JavierSabando.objects.get(id=id)
            objt.nombre = jd['nombre'] 
            objt.apellido = jd['apellido']
            objt.edad = jd['edad']
            objt.sexo = jd['sexo']
            objt.telefono = jd['telefono']
            objt.direccion = jd['direccion']
            objt.save()
            datos = {'message': "Success"}
        else:   
            datos= {'message':"Person not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        objts = list(JavierSabando.objects.filter(id=id).values())
        if len(objts) > 0:
            JavierSabando.objects.filter(id=id).delete()
            datos = {'message': "Deleted"}
        else:   
            datos= {'message':"Person not found..."}
        return JsonResponse(datos)