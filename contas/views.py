from django.shortcuts import render, redirect
import datetime
from .models import Transacao
from .forms import TransacaoForm
from django.http import HttpResponse
# Create your views here.

def home(request):
    now = datetime.datetime.now()
    # html = "Agora é: %s." % now
    return render(request, 'contas/home.html', {'now':now})

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    return render(request, 'contas/form.html', {'form':form})


def update(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    return render(request, 'contas/form.html', {'form': form, 'transacao':transacao})

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')