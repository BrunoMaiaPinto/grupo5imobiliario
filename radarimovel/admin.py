from django.contrib import admin

# Register your models here.
from .models import Agencias, Angaria, Consultores, Imovel, Localizacao, Proprietario, RedeAgencia

class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ('zona', 'distrito', 'concelho', 'freguesia')

admin.site.register(Agencias)
admin.site.register(Angaria)
admin.site.register(Consultores)
admin.site.register(Imovel)
admin.site.register(Localizacao, LocalizacaoAdmin)
admin.site.register(Proprietario)
admin.site.register(RedeAgencia)