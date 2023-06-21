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


def delete(id):
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

def listas(request):
    listas = Lista.objects.all
    context = {
        'listas': listas,
    }
    return render(request, 'listas.html', context)


def receitas(request):
    produtos = Produto.objects.all
    listas = Lista.objects.all
    categorias = Categoria.objects.all
    tagReceita = TagReceita.objects.all
    receitas = Receita.objects.all
    context = {
        'produtos': produtos,
        'listas': listas,
        'categorias': categorias,
        'tagReceita': tagReceita,
        'receitas': receitas,
    }
    return render(request, 'receitas.html', context)

def page_produto(request):
    produtos = Produto.objects.all()
    categoria = Categoria.objects.all()
    context = {
        "produtos": produtos,
        "categoria": categoria,
    }

    return render (request,'produtos.html', context)

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
    return redirect(page_produto)

def delete_produto(request, pk):
    produto = Produto.objects.get(id = pk)
    produto.delete()
    return HttpResponseRedirect('/produtos/') 

def show_produto(request,pk):
    produto = Produto.objects.get(id = pk)
    categoria = Categoria.objects.all()
    context = {
        "produto": produto,
        "categoria": categoria
    }
    return render(request, 'edit_produto.html', context)



def edit_produto(request,pk):
    if request.method == 'POST':
        produto = Produto.objects.get(id = pk)
        produto.nome = request.POST['nome']
        produto.descricao = request.POST['descricao']
        categoria = Categoria.objects.get(id = request.POST['categoria'])

        produto.categoria = categoria
        produto.save()

        return redirect(page_produto)
    
def add_lista(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        data = Lista(
            nome = nome,
        )
        data.save()
    return HttpResponseRedirect('/listas/')

def delete_lista(request,pk):
    lista = Lista.objects.filter(id = pk)
    lista.delete()
    return HttpResponseRedirect('/listas/') 

def edit_lista(request,pk):
    if request.method == 'POST':
        lista = Lista.objects.get(id = pk)
        lista.nome = request.POST['nome']
        lista.save()
    return redirect(listas) 

def add_prod_in_lista(request, pk):
    if request.method == 'POST':
        lista = Lista.objects.get(id = pk)
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
    return HttpResponseRedirect('/show_lista/'+str(pk)+'/')

def show_lista(request,pk):
    lista_produto = Lista_produto.objects.filter(lista__id=pk)
    lista = Lista.objects.get(id=pk)
    produto = Produto.objects.all()

    context = {
        'lista_produto': lista_produto,
        'lista': lista,
        'produto': produto,
        'pk':pk,
    }
    return render(request, 'edit_lista.html', context)

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
    return HttpResponseRedirect('/receitas/')

def delete_receita(request, pk):
    receita = Receita.objects.get(id = pk)
    receita.delete()
    return HttpResponseRedirect('/receitas/')  

def edit_receita(request, pk):
    if request.method == 'POST':
        receita = Receita.objects.get(id = pk)
        receita.nome = request.POST['nome']
        receita.descricao = request.POST['descricao']
       
        receita.save()
    return redirect(receitas)


def add_prod_in_receita(request, pk):
    if request.method == 'POST':
        receita = Receita.objects.get(id = pk)
        produto = Produto.objects.get(id = request.POST['idProduto'])
        quantidade = request.POST['quantidade']
        data = ProdutoReceita(
            produto = produto,
            receita = receita,
            quantidade = quantidade,
        )
        data.save()
    return HttpResponseRedirect('/showReceita/'+str(pk)+'/')


def show_receita(request,pk):
    receitaProduto = ProdutoReceita.objects.filter(receita__id=pk)
    receita = Receita.objects.get(id=pk)
    produto = Produto.objects.all()
    context = {
        'receitaProduto': receitaProduto,
        'receita': receita,
        'produto': produto,
        'pk':pk,
    }
    return render(request, 'edit_receita.html', context)

def page_mercado(request):
    supermercado = Supermercado.objects.all()

    context={
            'supermercado': supermercado,
        }
    return render (request,'mercados.html', context)

def add_mercado(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        endereco = request.POST['endereco']
        supermercado = Supermercado.objects.all()

        context={
            'supermercado': supermercado,
        }

        Supermercado.objects.create(nome=nome,endereco=endereco)
      
    return redirect('page_mercado')