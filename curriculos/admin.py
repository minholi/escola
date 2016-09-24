from django.contrib import admin
from curriculos.models import *

class PeriodoLetivoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'periodo', 'inicio', 'termino', 'proximo')

class CurriculoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'inicio', 'curso', 'turno')
    
admin.site.register(PeriodoLetivo, PeriodoLetivoAdmin)
admin.site.register(Curriculo, CurriculoAdmin)
