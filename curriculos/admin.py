from django.contrib import admin
from curriculos.models import *

class SerieInline(admin.TabularInline):
    model = Serie
    
class GradeInline(admin.TabularInline):
    model = Grade

class PeriodoLetivoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'periodo', 'inicio', 'termino', 'proximo')

class CurriculoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'inicio', 'curso', 'turno')
    inlines = [SerieInline, GradeInline]
    
admin.site.register(PeriodoLetivo, PeriodoLetivoAdmin)
admin.site.register(Curriculo, CurriculoAdmin)
