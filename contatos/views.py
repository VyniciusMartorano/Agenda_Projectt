from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


# Create your views here.

def index(request):
    #ordenar os contatos pelo nome, filtrar para mostrar os que tem mostrar = True
    contatos = Contato.objects.order_by('nome').filter(
        mostrar=True
    )
    #limitar a pagina a so ter 2 contatos
    paginator = Paginator(contatos,2)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request,'contatos/index.html',{
        'contatos': contatos
    })

def ver_contato(request,contato_id):
    #get_obj... captura o objeto pelo id, se por acaso o id não existir ele levanta a pagina 404
    contato = get_object_or_404(Contato,id=contato_id)

    if not contato.mostrar:
        raise Http404()

    return render(request,'contatos/ver_contato.html',{
        'contato': contato
    })


def busca(request):

    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(
            request,
            messages.ERROR,
            'Campo não pode estar vázio'
        )
        messages.add_message(request,messages.SUCCESS, 'Mensagem de sucesso!')
        return redirect('index')

    #value simula um campo vazio para poder concatenar
    campos = Concat('nome', Value(' '),'sobrenome')


    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo))
    #filtrar OU pelo nome OU pelo sobrenome OU pelo telefone OU pelo nome E sobrenome



    # ordenar os contatos pelo nome, filtrar para mostrar os que tem mostrar = True
    #icontains procura valores que contenham a chave procurada
    '''contatos = Contato.objects.order_by('-id').filter(
        nome__icontains=termo,
        mostrar=True
    )'''
    # limitar a pagina a so ter 2 contatos
    paginator = Paginator(contatos, 2)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })










