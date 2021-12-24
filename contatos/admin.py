from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    #mostrar infos no display
    list_display = ('id','nome','sobrenome','telefone','email',
                    'data_criacao','categoria','mostrar')
    #criar link em cada uma das chaves abaixo
    list_display_links = ('id','nome','sobrenome')
    #criar a opção de filtrar pelas seguintes chaves
    list_filter = ('nome','sobrenome','id')
    #exibe apenas x contatos por pagina
    list_per_page = 10
    #cria uma barra de pesquisa que pesquisa pelas seguintes chaves:
    search_fields = ('nome','sobrenome')
    #itens que podem ser editados pelo lado de fora
    list_editable = ('telefone','mostrar')
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
