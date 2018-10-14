from django.shortcuts import render
from .models import Equipo
from django.views import generic

def index(request):
	return render(request, 'estadisticas/index.html')

class ligaBBVA(generic.ListView):
	template_name = 'estadisticas/ligaBBVA.html'
	context_object_name = 'equipos'

	def get_queryset(self):
		return Equipo.objects.filter(liga=1).order_by('nombre')

class liga123(generic.ListView):
	template_name = 'estadisticas/liga123.html'
	context_object_name = 'equipos'

	def get_queryset(self):
		return Equipo.objects.filter(liga=2).order_by('nombre')
