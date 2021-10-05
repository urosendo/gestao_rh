from django.urls import path
from .views import (FuncionarioList,
                    FuncionarioEdit,
                    FuncionarioDelete,
                    FuncionarioCreate)


urlpatterns = [
    path('',FuncionarioList.as_view(), name='list_funcionarios'),
    path('novo/',FuncionarioCreate.as_view(), name='create_funcionario'),
    path('edit/<int:pk>/',FuncionarioEdit.as_view(), name='update_funcionario'),
    path('delete/<int:pk>/',FuncionarioDelete.as_view(), name='delete_funcionario'),
]