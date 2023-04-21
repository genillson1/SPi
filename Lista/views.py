from django.http import HttpResponseRedirect
from django.shortcuts import *
from .models import Categoria
from Lista.models import Produto, Categoria, Lista, Lista_produto
from Lista.models import Receita, TagReceita, ProdutoReceita, Supermercado


def home(request):
    categorias = Categoria.objects.all()
    return render(request, "index.html", {"categorias": categorias})

def salvar(request):
    nome = request.POST.get("nome")
    Categoria.objects.create(nome=nome)
    categorias = Categoria.objects.all()
    return render(request, "index.html", {"categorias": categorias})

def editar(request, id):
    idCategoria = Categoria.objects.get(id=id)
    return render(request, "update.html", {"categorias": idCategoria})

def update(request, id):
    categoria = request.POST.get("nome")
    categorias = Categoria.objects.get(id=id)
    categorias.nome = categoria
    categorias.save()
    return redirect(home)


def delete(request, id):
    Categorias = Categoria.objects.get(id=id)
    Categorias.delete()
    return redirect(home)


def index(request):
    produtos = Produto.objects.all
    lista = Lista.objects.all
    categorias = Categoria.objects.all
    tagReceita = TagReceita.objects.all
    receita = Receita.objects.all
    context = {
        'produtos': produtos,
        'lista': lista,
        'categorias': categorias,
        'tagReceita': tagReceita,
        'receita': receita,
    }
    return render(request, 'index.html', context)

def add_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        categoria = Categoria.objects.get(id = request.POST['categoria'])
        data = Produto(
            nome = nome,
            descricao = descricao,
            categoria = categoria
        )
        data.save()
    return HttpResponseRedirect('/')

def delete_produto(request, pk):
    produto = Produto.objects.get(id = pk)
    produto.delete()
    return HttpResponseRedirect('/') 


def edit_produto(request):
    if request.method == 'POST':
        produto = Produto.objects.get(id = request.POST['id'])
        produto.nome = request.POST['nome']
        produto.descricao = request.POST['descricao']
        categoria = Categoria.objects.get(id = request.POST['categoria'])
        produto.categoria = categoria
        produto.save()
    return HttpResponseRedirect('/') 

def add_lista(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        data = Lista(
            nome = nome,
        )
        data.save()
    return HttpResponseRedirect('/')

def delete_lista(request, pk):
    lista = Lista.objects.get(id = pk)
    lista.delete()
    return HttpResponseRedirect('/listas/') 


def edit_lista(request):
    if request.method == 'POST':
        lista = Lista.objects.get(id = request.POST['id'])
        lista.nome = request.POST['nome']
        lista.save()
    return HttpResponseRedirect('/') 

def add_prod_in_lista(request):
    if request.method == 'POST':
        lista = Lista.objects.get(id = request.POST['idLista'])
        produto = Produto.objects.get(id = request.POST['idProduto'])
        quantidade = request.POST['quantidade']
        second_option = Produto.objects.get(id = request.POST['idSecondOption'])
        importancia = request.POST['importancia']
        data = Lista_produto(
            produto = produto,
            lista = lista,
            quantidade = quantidade,
            produto_second_option = second_option,
            importancia = importancia,
        )
        data.save()
    return HttpResponseRedirect('/')


def show_lista(request,pk):
    lista_produto = Lista_produto.objects.filter(lista__id=pk)
    context = {
        'lista_produto': lista_produto,
    }
    return render(request, 'verLista.html', context)

def add_receita(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        print(nome)
        descricao = request.POST['descricao']
  
        data = Receita(
            nome = nome,
            descricao = descricao,
            
        )
        data.save()
    return HttpResponseRedirect('/')

def delete_receita(request, pk):
    receita = Receita.objects.get(id = pk)
    receita.delete()
    return HttpResponseRedirect('/') 

def edit_receita(request):
    if request.method == 'POST':
        receita = Receita.objects.get(id = request.POST['id'])
        receita.nome = request.POST['nome']
        receita.descricao = request.POST['descricao']
        receita.save()
    return HttpResponseRedirect('/')


def add_prod_in_receita(request):
    if request.method == 'POST':
        receita = Receita.objects.get(id = request.POST['idReceita'])
        produto = Produto.objects.get(id = request.POST['idProduto'])
        quantidade = request.POST['quantidade']
        data = ProdutoReceita(
            produto = produto,
            receita = receita,
            quantidade = quantidade,
        )
        data.save()
    return HttpResponseRedirect('/')


def show_receita(request,pk):
    receitaProduto = ProdutoReceita.objects.filter(receita__id=pk)
    context = {
        'receitaProduto': receitaProduto,
    }
    return render(request, 'showReceita.html', context)

def add_mercado(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        print(nome)
        endereco = request.POST['endereco']
  
        data = Supermercado(
            nome = nome,
            endereco = endereco,
            
        )
        data.save()
    return HttpResponseRedirect('/')

