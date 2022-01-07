from django.contrib import admin
from .models import *
from .models import Oficios

# Register your models here.

#admin.site.register(Proprietario)
#admin.site.register(Veiculo)
#admin.site.register(Acessorio)


class OficiosAdmin(admin.ModelAdmin):
    list_filter = ["orgao", "temaofi"]

admin.site.register(Oficios, OficiosAdmin)


