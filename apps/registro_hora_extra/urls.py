from django.urls import path
from .views import (HoraExtraList,
                    HoraExtraEdit,
                    HoraExtraDelete,
                    HoraExtraCreate,
                    HoraExtraEdit_base)


urlpatterns = [
    path('',HoraExtraList.as_view(), name='list_hora_extra'),
    path('novo/', HoraExtraCreate.as_view(), name='create_hora_extra'),
    path('edit/funcionario/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('edit/<int:pk>/', HoraExtraEdit_base.as_view(), name='update_hora_extra_base'),
    path('delete/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),

]