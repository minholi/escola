from django.db import models

class Turno(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()

    class Meta:
        verbose_name = 'Turno'
    
    def __str__(self):
        return self.nome    


class Curso(models.Model):
    nome = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Curso'
    
    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    horas_aula = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    horas_atividade = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    tem_nota = models.BooleanField(default=True)
    tem_frequencia = models.BooleanField(default=True)
    nota_minima = models.DecimalField(max_digits=3, decimal_places=1, default=6.0)
    frequencia_minima = models.DecimalField(max_digits=5, decimal_places=2, default=75.00)
    ativa = models.BooleanField(default=True)
    
    def _get_carga_horaria(self):
        "Retorna a carga horária total da disciplina."
        return self.horas_aula + self.horas_atividade
    _get_carga_horaria.short_description = 'Carga Horária'
    carga_horaria = property(_get_carga_horaria)
    
    class Meta:
        verbose_name = 'Disciplina'
    
    def __str__(self):
        return self.nome