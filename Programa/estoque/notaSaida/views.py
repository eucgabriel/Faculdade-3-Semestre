from django.http import HttpResponse
from django.shortcuts import render, redirect

from produto.models import Produtos
from .models import NotasSaidas
from .forms import NotasSaidasForm

def notaSaidaList(request):
    nota_saida = NotasSaidas.objects.all()
    template_name = 'notaSaidaList.html'
    context = {
        'nota_saida': nota_saida,
    }
    return render(request, template_name, context)

def notaSaidaNew(request):
    if request.method == "POST":
        form = NotasSaidasForm(request.POST)
        if form.is_valid():
            form.save(commit=False)

            form.cleaned_data['produto'].quantidade = form.cleaned_data['produto'].quantidade - form.cleaned_data['quantidade']

            form.cleaned_data['produto'].preco = form.cleaned_data['preco']
            form.cleaned_data['produto'].save_base()
            
            form.save()
            
            return redirect('notaEntrada:notaEntradaList')
    else:
        form = NotasSaidasForm()
        template_name = 'notaSaidaNew.html'
        context = {
            'form': form
        }
        return render(request, template_name, context)

def notaSaidaDelete(request, pk):
    saida = NotasSaidas.objects.get(id=pk)
    print("Id NE: ", saida.id)
    print("Qt NE: ", saida.quantidade)
    print("produto: ", saida.produto)
    print("Id produto", saida.produto.id)
    print("Quantidade produto: ", saida.produto.quantidade)

    saida.produto.quantidade = saida.produto.quantidade - saida.quantidade
    saida.produto.save()
    saida.delete()
    template_name = 'notaSaidaDelete.html'
    context = {
        'mensagem': 'Deletado com sucesso!!! AHAHAH'
    }
    return render(request, template_name, context)


def notaSaidaUpdate(request, pk):
    saida = NotasSaidas.objects.get(id=pk)
    quantidade_nota = saida.quantidade 
    if request.method == 'POST':
        form = NotasSaidasForm(request.POST, instance=saida)
        if form.is_valid():
            form.save(commit=False)

            diferenca_quantidade = quantidade_nota - form.cleaned_data['quantidade']
            print("Diferença: ", diferenca_quantidade, quantidade_nota, form.cleaned_data['quantidade'])

            form.cleaned_data['produto'].quantidade = form.cleaned_data['produto'].quantidade  - diferenca_quantidade
            
            # form.cleaned_data['produto'].save_base()
            # form.save()
            return redirect('notaSaida:notaSaidaList')
    else:
        template_name = 'NotaSaidaUpdate.html'
        context = {
            'form': NotasSaidasForm(instance=saida),
            'pk': pk
        }
        return render(request, template_name, context)
