import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm
from django.views import View

class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
        return queryset

class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo','funcionario','horas']


class HoraExtraEdit_base(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo','funcionario','horas']
    #success_url = reverse_lazy('list_hora_extra')

    def get_success_url(self):
        return reverse_lazy('update_hora_extra_base', args=[self.object.pk])


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user':self.request.user})
        return kwargs


class UtilizouHoraExtra(View):

    def post(self, *args, **kwargs):

        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        if registro_hora_extra.utilizada == False:
            registro_hora_extra.utilizada = True
            label_button = 'Marcar como não utilizada'
        else:
            registro_hora_extra.utilizada = False
            label_button = 'Marcar como utilizada'

        registro_hora_extra.save()

        empregado = self.request.user.funcionario


        response = json.dumps(
            {'mensagem':'Requisição Executada 2',
             'horas':float(empregado.total_horas_extra),
             'label_button':label_button})

        return HttpResponse(response, content_type='application/json')
