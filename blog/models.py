from django.db import models
from django.utils import timezone

class Aluno(models.Model):
	matricula = models.CharField(max_length = 30)
	nome = models.CharField(max_length = 120, null = False)
	dt_nasc = models.DateField(null=False)
	cpf = models.CharField(max_length=11, primary_key = True)
	telefone = models.IntegerField(null = False)
	ender = models.CharField(max_length = 120, null = False)

	def __str__(self):
		return str(self.matricula)


class Livro(models.Model):
	nome = models.CharField(max_length=100, null = False)
	isbn = models.CharField(max_length = 30, null = False, primary_key = True)
	desc = models.CharField(max_length=200, null = False)
	autor = models.CharField(max_length=120, null = False)

	def __str__(self):
		return str(self.nome)

class Atendente(models.Model):
	nome = models.CharField(max_length=120, null = False)
	dt_nasc = models.DateField(null=False)
	cpf = models.CharField(max_length = 11, primary_key = True)
	tel = models.IntegerField(null = False)
	ender = models.CharField(max_length = 120, null = False)

	def __str__(self):
		return str(self.nome)

class Emprestimo(models.Model):
	cod_emp = models.IntegerField(primary_key = True)
	matricula = models.ForeignKey('Aluno')
	livro = models.ForeignKey('Livro')
	atendente = models.ForeignKey('Atendente')
	dt_emp = models.DateField(null=False)

	def __str__(self):
		return str(self.cod_emp)