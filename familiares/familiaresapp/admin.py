from django.contrib import admin
from .models import Familiares

class FamiliaresAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','edad','fecha_de_nacimiento')

admin.site.register(Familiares,FamiliaresAdmin)

