from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    contatos = Contato.objects.order_by('nome')
    paginator = Paginator(contatos, 1)  # Show 20 contacts per page

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



