from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm

class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
        return queryset

class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo','funcionario','horas']


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


    git filter - branch - -env - filter if ["$GIT_AUTHOR_NAME" = "Ullysses"] then export GIT_AUTHOR_NAME="Ullysses" GIT_AUTHOR_EMAIL="urozendo@gmail.com" fi
