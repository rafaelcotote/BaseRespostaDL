from django.contrib import admin
from .models import *
from .models import Oficios
from .models import Proprietario
from .models import Veiculo
from .models import Temes
from import_export.admin import ExportMixin
from import_export.formats import base_formats

# Register your models here.

#admin.site.register(Proprietario)
#admin.site.register(Veiculo)
#admin.site.register(Acessorio)
admin.site.register(Temes)

class TemesAdmin(admin.ModelAdmin):
    search_fields = ["orgao", "questionamento", "conteudo", "titulo_oficio", "status_oficio"]
    list_display = ["titulo_oficio", "oficios", "orgao", "status_oficio"]
    list_filter = ["orgao", "temaofi", "questionamento", "conteudo", "titulo_oficio", "status_oficio"]
    icon_name = "list"

class OficiosAdmin(ExportMixin, admin.ModelAdmin):
    Oficios = 'Ofício'
    icon_name = 'markunread'
    list_display = ["titulo_oficio", "orgao", "get_temm", "status_oficio", "recebimento", "responsavel_envio"]
    list_filter = ["orgao", "status_oficio", "temm", "envio", "recebimento", "responsavel_envio"]
    search_fields = ["orgao", "questionamento", "conteudo", "titulo_oficio", "status_oficio"]

    def get_export_formats(self):
        formats = (
            base_formats.CSV,
            base_formats.XLSX
        )
        return [f for f in formats if f().can_export()]

admin.site.register(Oficios, OficiosAdmin)

class ConsultoriaAdmin(admin.ModelAdmin):
    icon_name = 'folder'