from django.db import models
from basico.models import Curso, Turno, Disciplina
from smart_selects.db_fields import ChainedForeignKey
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
        return u'%s de %s' % (self.nome, self.curso)
        

class Serie(models.Model):
    curriculo = models.ForeignKey(Curriculo, verbose_name='currículo')
    serie = models.IntegerField(verbose_name='série')
    descricao = models.CharField(max_length=255, verbose_name='descrição')
    
    class Meta:
        verbose_name = 'Série'
        
    def __str__(self):
        return self.descricao
        
        
class Componente(models.Model):
    curriculo = models.ForeignKey(Curriculo)
    disciplina = models.ForeignKey(Disciplina)
    serie = ChainedForeignKey(
        Serie, 
        chained_field="curriculo",
        chained_model_field="curriculo", 
        show_all=False, 
        auto_choose=True,
        sort=True,
        verbose_name='série'
    )
    obrigatorio = models.BooleanField(default=True, verbose_name='obrigatório')
    
    class Meta:
        unique_together = ('curriculo', 'disciplina')
        
    def __str__(self):
        return u'%s de %s' % (self.disciplina, self.curriculo)
        
        
class Turma(models.Model):
    nome = models.CharField(max_length=255)
    disciplina = models.ForeignKey(Disciplina)
    periodo = models.ForeignKey(PeriodoLetivo)
    turno = models.ForeignKey(Turno)
    
    class Meta:
        pass
        
    def __str__(self):
        return self.nome