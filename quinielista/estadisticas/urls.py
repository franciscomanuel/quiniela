from django.urls import path

from . import views

app_name = 'estadisticas'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:pk>/ligaBBVA/', views.ligaBBVA.as_view(), name='ligaBBVA'),
	path('<int:pk>/liga123/', views.liga123.as_view(), name='liga123')
]