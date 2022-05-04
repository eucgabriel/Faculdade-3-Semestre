from django.contrib import admin
from .models import Pessoas
# Register your models here.


class PessoasAmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'idade']
    ordering = ['-nome']
    search_fields = ['nome']
    list_filter = ['idade']
    list_editable = ['telefone', 'idade']


admin.site.register(Pessoas, PessoasAdmin)
