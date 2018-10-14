from django.db import models

class Estadio(models.Model):
	def __str__(self):
		return self.nombre

	nombre = models.CharField(max_length=50)

class Liga(models.Model):
	def __str__(self):
		return self.nombre

	nombre = models.CharField(max_length=50)

class Equipo(models.Model):
	def __str__(self):
		return self.nombre

	nombre = models.CharField(max_length=50)
	estadio = models.OneToOneField(Estadio, on_delete=models.CASCADE, null=True)
	liga = models.ForeignKey(Liga, on_delete=models.CASCADE, null=True)

class Encuentro(models.Model):

	def __str__(self):
		return self.equipo1.nombre + " vs " + self.equipo2.nombre

	jornada = models.PositiveIntegerField(default=0)
	fecha = models.DateField('Fecha')
	hora = models.TimeField()
	estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE)
	liga = models.ForeignKey(Liga, on_delete=models.CASCADE, null=True)
	equipo1 = models.ForeignKey(Equipo, related_name='equipo1', on_delete=models.CASCADE, null=True)
	equipo2 = models.ForeignKey(Equipo, related_name='equipo2', on_delete=models.CASCADE, null=True)
	golesLocal = models.PositiveIntegerField(default=0)
	golesVisitante = models.PositiveIntegerField(default=0)
