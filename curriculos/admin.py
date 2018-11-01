from django.contrib import admin
from escola.admin import admin_site
<<<<<<< HEAD
from django.core.urlresolvers import resolve
=======
>>>>>>> origin/master
from curriculos.models import *

class SerieInline(admin.TabularInline):
    model = Serie
    
class ComponenteInline(admin.TabularInline):
    model = Componente

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(ComponenteInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'serie':
            resolved = resolve(request.path_info)
            field.queryset = field.queryset.filter(curriculo=resolved.args[0])
        return field

class PeriodoLetivoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'periodo', 'inicio', 'termino', 'proximo')

class CurriculoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'inicio', 'curso', 'turno')
    inlines = [SerieInline, ComponenteInline]
    
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'disciplina', 'periodo', 'turno')
    
admin_site.register(PeriodoLetivo, PeriodoLetivoAdmin)
admin_site.register(Curriculo, CurriculoAdmin)
admin_site.register(Turma, TurmaAdmin)