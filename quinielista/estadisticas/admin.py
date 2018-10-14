from django.contrib import admin

from .models import Equipo, Estadio, Encuentro, Liga

"""class Encuentros(admin.ModelAdmin):"""

"""class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'question_text']
	fieldsets = [
		(None, 				 {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)"""

class EquipoInline(admin.TabularInline):
	model = Equipo
	extra = 3

class LigaAdmin(admin.ModelAdmin):
	inlines = [EquipoInline]

	def get_queryset(self, request):
		return super(LigaAdmin, self).get_queryset(request).order_by('nombre')

class EquipoAdmin(admin.ModelAdmin):
	fields = ['nombre', 'estadio', 'liga']
	list_display = ('nombre', 'estadio', 'liga')
	list_filter = ['liga']

	def get_queryset(self, request):
		return super(EquipoAdmin, self).get_queryset(request).order_by('nombre')

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'estadio':
			kwargs['queryset'] = Estadio.objects.all().order_by('nombre')
		return super(EquipoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class EstadioAdmin(admin.ModelAdmin):
	def get_queryset(self, request):
		return super(EstadioAdmin, self).get_queryset(request).order_by('nombre')

class EncuentroAdmin(admin.ModelAdmin):
	list_display = ('jornada', 'equipo1', 'equipo2', 'golesLocal', 'golesVisitante', 'fecha', 'hora', 'liga')
	list_filter = ['jornada', 'liga']

	#def formfield_for_foreignkey(self, db_field, request, **kwargs):
	#	if db_field.name == 'equipo1':
	#		kwargs['queryset'] = Equipo.objects.filter(liga=1).order_by('nombre')
	#	return super(EncuentroAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Estadio, EstadioAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Encuentro, EncuentroAdmin)
admin.site.register(Liga, LigaAdmin)
