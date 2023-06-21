from django.urls import path
from . import views
from .views import *


urlpatterns = [

    path('', home),
    path('salvar/', salvar, name= "salvar"),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),

    path('', views.index, name='index'),
    path('listas/', views.listas, name='listas'),
    path('receitas/', views.receitas, name='receitas'),
    path('add_produto/', views.add_produto, name='add_produto'),
    path('produtos/', views.page_produto, name='page_produto'),

    path('delete_produto/<int:pk>/', views.delete_produto, name='delete_produto'),
    path('showProduto/<int:pk>/', views.show_produto, name='show_produto'),
    path('edit_produto/<int:pk>/', views.edit_produto, name='edit_produto'),



    path('add_lista/', views.add_lista, name='add_lista'),
    path('delete_lista/<int:pk>/', views.delete_lista, name='delete_lista'),
    path('edit_lista/<int:pk>/', views.edit_lista, name='edit_lista'),
    path('add_prod_in_lista/', views.add_prod_in_lista, name='add_prod_in_lista'),

    
    path('show_lista/<int:pk>/', views.show_lista, name='show_lista'), 
    path('showReceita/<int:pk>/', views.show_receita, name='show_receita'), 

    path('add_receita/', views.add_receita, name='add_receita'),
    path('delete_receita/<int:pk>/', views.delete_receita, name='delete_receita'),
    path('edit_receita/<int:pk>/', views.edit_receita, name='edit_receita'),
    path('add_prod_in_receita/', views.add_prod_in_receita, name='add_prod_in_receita'),

    path('add_mercado/', views.add_mercado , name='add_mercado'),
    path('page_mercado/', views.page_mercado, name='page_mercado'),
   
]
