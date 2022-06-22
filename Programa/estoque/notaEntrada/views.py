from django.http import HttpResponse
from django.shortcuts import render, redirect

from produto.models import Produtos
from .models import NotasEntradas
from .forms import NotasEntradasForm

def notaEntradaList(request):
    nota_entrada = NotasEntradas.objects.all()
    template_name = 'notaEntradaList.html'
    context = {
        'nota_entrada': nota_entrada,
    }
    return render(request, template_name, context)

def notaEntradaNew(request):
    if request.method == "POST":
        form = NotasEntradasForm(request.POST)
        if form.is_valid():
            form.save(commit=False)

            form.cleaned_data['produto'].quantidade = form.cleaned_data['produto'].quantidade + form.cleaned_data['quantidade']

            form.cleaned_data['produto'].preco = form.cleaned_data['preco']
            form.cleaned_data['produto'].save_base()
            
            form.save()
            
            return redirect('notaEntrada:notaEntradaList')
    else:
        form = NotasEntradasForm()
        template_name = 'notaEntradaNew.html'
        context = {
            'form': form
        }
        return render(request, template_name, context)

def notaEntradaDelete(request, pk):
    entrada = NotasEntradas.objects.get(id=pk)
    print("Id NE: ",entrada.id)
    print("Qt NE: ", entrada.quantidade)
    print("produto: ", entrada.produto)
    print("Id produto", entrada.produto.id)
    print("Quantidade produto: ", entrada.produto.quantidade)

    entrada.produto.quantidade = entrada.produto.quantidade - entrada.quantidade
    entrada.produto.save()
    entrada.delete()
    template_name = 'notaEntradaDelete.html'
    context = {
        'mensagem': 'Deletado com sucesso!!! AHAHAH'
    }
    return render(request, template_name, context)


def notaEntradaUpdate(request, pk):
    entrada = NotasEntradas.objects.get(id=pk)
    quantidade_nota = entrada.quantidade 
    if request.method == 'POST':
        form = NotasEntradasForm(request.POST, instance=entrada)
        if form.is_valid():
            form.save(commit=False)

            diferenca_quantidade = quantidade_nota - form.cleaned_data['quantidade']
            print("Diferença: ", diferenca_quantidade, quantidade_nota, form.cleaned_data['quantidade'])

            form.cleaned_data['produto'].quantidade = form.cleaned_data['produto'].quantidade  - diferenca_quantidade
            
            # form.cleaned_data['produto'].save_base()
            # form.save()
            return redirect('notaEntrada:notaEntradaList')
    else:
        template_name = 'NotaEntradaUpdate.html'
        context = {
            'form': NotasEntradasForm(instance=entrada),
            'pk': pk
        }
        return render(request, template_name, context)
