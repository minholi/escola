from django.contrib import admin
from curriculos.models import *

class PeriodoLetivoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'periodo', 'inicio', 'termino', 'proximo')

admin.site.register(PeriodoLetivo, PeriodoLetivoAdmin)
