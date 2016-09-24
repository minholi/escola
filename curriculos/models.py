from django.db import models
from basico.models import Curso, Turno
import datetime

# Popula o choices usado nos campos de ano
ANO_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+30)):
    ANO_CHOICES.append((r,r))

class PeriodoLetivo(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(verbose_name='descrição')
    ano = models.IntegerField(choices=ANO_CHOICES, default=datetime.datetime.now().year)
    periodo = models.IntegerField(verbose_name='período')
    inicio = models.DateField(verbose_name='início')
    termino = models.DateField(verbose_name='término')
    proximo = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='próximo', blank=True, null=True) # TODO: Criar validação (ano do próximo período >=)
    
    class Meta:
        verbose_name = 'Período Letivo'
        verbose_name_plural = 'Períodos Letivos'
    
    def __str__(self):
        return self.nome

        
class Curriculo(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(verbose_name='descrição')
    inicio = models.ForeignKey(PeriodoLetivo, verbose_name='início')
    curso = models.ForeignKey(Curso)
    turno = models.ForeignKey(Turno)
    
    class Meta:
        verbose_name = 'Currículo'
    
    def __str__(self):
        return self.nome