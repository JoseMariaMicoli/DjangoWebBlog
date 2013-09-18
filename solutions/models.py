from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Solution(models.Model):
	title = models.CharField(max_length=100)
	desc = models.TextField(max_length=200)
	body = models.TextField()
	create = models.DateTimeField()
	oferta = models.TextField()
	slug = models.SlugField(max_length=100, blank=True, unique=True)

	def get_absolute_url(self):
		return reverse('solution', kwargs = {'slug': self.slug})
	
	def __unicode__(self):
		return self.title

class ClientReport(models.Model):
	solucao = models.ForeignKey('Solution')
	nome = models.CharField(max_length=100)
	sobrenome = models.CharField(max_length=100)
	telefone = models.CharField(max_length=30)
	rua = models.CharField(max_length=100)
	numero = models.CharField(max_length=10)
	bairro = models.CharField(max_length=100)
	cidade = models.CharField(max_length=100)
	cep = models.CharField(max_length=20)
	empresa = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	campo_de_pergunta = models.TextField()
	data = models.DateTimeField()

	def __unicode__(self):
		return self.nome
	
	

# SIGNALS

from django.db.models import signals
from utils.signals_common import slug_pre_save

signals.pre_save.connect(slug_pre_save, sender=Solution)
