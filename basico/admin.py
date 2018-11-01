from django.contrib import admin
from escola.admin import admin_site
from basico.models import *

class DisciplinaAdmin(admin.ModelAdmin):
    readonly_fields = ('carga_horaria',)
    list_display = ('nome', 'horas_aula', 'horas_atividade', 'carga_horaria', 'tem_nota', 'tem_frequencia', 'ativa')
    list_filter = ('ativa',)
    fieldsets = (
        (None, {
            'fields': ('nome', 'horas_aula', 'horas_atividade', 'ativa')
        }),
        ('Avaliação', {
            'classes': ('collapse',),
            'fields': ('tem_nota', 'tem_frequencia', ('nota_minima', 'frequencia_minima')),
        }),
    )

admin_site.register(Curso)
admin_site.register(Turno)
admin_site.register(Disciplina, DisciplinaAdmin)