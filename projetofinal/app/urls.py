from django.urls import path, re_path
from .views import *
from django.contrib import admin

urlpatterns = [
    #re_path(r'^veiculo/listar/$', listar_veiculo, name='listar_veiculo'),
    re_path(r'^veiculo/listar/(?P<categoria>[\w\-]+)/$', listar_veiculo, name='listar_veiculo'),
    re_path(r'^veiculo/perfil/(?P<pk>[0-9]+)', perfil_veiculo, name='perfil_veiculo'),
]