from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse
from django.db.models import Sum
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)


    def get_absolute_url(self):
        return reverse('list_funcionarios')


    @property
    def total_horas_extra(self):
        total = self.registrohoraextra_set.filter(utilizada=False).aggregate(Sum('horas'))['horas__sum']
        return total or 0

    def __str__(self):
        return self.nome

