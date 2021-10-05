from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from django.shortcuts import render

from .models import Funcionario

# Create your views here.

def home(request):
    return HttpResponse('Teste')


class FuncionarioList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_logada)
        return queryset

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit = False)
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(
            username = ''.join(funcionario.nome.split(' '))
        )
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)


