from atexit import register
from django.contrib import admin
from .models import Alfabeto

# Register your models here.

class AlfabetoAdmin(admin.ModelAdmin):
    list_display = ('id_letra', 'letra', 'idioma', 'letra_convertida')

admin.site.register(Alfabeto, AlfabetoAdmin)