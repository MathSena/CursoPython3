from django.core import paginator
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages

# Create your views here.
def index(request):
    #messages.add_message(request, messages.ERROR, 'Ocorreu um erro.')
    contatos = Contato.objects.order_by('nome')
    paginator = Paginator(contatos, 20)  # Show 20 contacts per page

    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html',{
        'contatos': contatos

    })

def ver_contato(request, contato_id):
    #contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)

    return render(request, 'contatos/ver_contato.html',{
        'contato': contato

    })

def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(
            request,
            messages.ERROR,
            'Campo termo não pode ficar vazio'
        )
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains =termo)| Q(telefone__icontains=termo)
    )

    paginator = Paginator(contatos,20)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html',{
        'contatos': contatos

    })


