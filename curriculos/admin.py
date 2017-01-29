from django.contrib import admin
from curriculos.models import *

class SerieInline(admin.TabularInline):
    model = Serie
    
class ComponenteInline(admin.TabularInline):
    model = Componente

class PeriodoLetivoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'periodo', 'inicio', 'termino', 'proximo')

class CurriculoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'inicio', 'curso', 'turno')
    inlines = [SerieInline, ComponenteInline]
    
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'disciplina', 'periodo', 'turno')
    
admin.site.register(PeriodoLetivo, PeriodoLetivoAdmin)
admin.site.register(Curriculo, CurriculoAdmin)
admin.site.register(Turma, TurmaAdmin)