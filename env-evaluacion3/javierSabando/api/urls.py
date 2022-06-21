from django.urls import path
from .views import JavierSabandoView, listPerson, redirect_view

urlpatterns = [
    path('', redirect_view),
    path('api/', JavierSabandoView.as_view(), name='person'),
    path('api/<int:id>', JavierSabandoView.as_view(), name='person'),
    path('lista/', listPerson.as_view(), name='person_list'),
]