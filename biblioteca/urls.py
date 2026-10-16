from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # Autores
    path("autores/", views.autor_listar, name="autor_listar"),
    path("autores/novo/", views.autor_criar, name="autor_criar"),
    path("autores/<int:pk>/", views.autor_detalhe, name="autor_detalhe"),
    path("autores/<int:pk>/editar/", views.autor_editar, name="autor_editar"),
    path("autores/<int:pk>/excluir/", views.autor_excluir, name="autor_excluir"),
    # Livros
    path("livros/", views.livro_listar, name="livro_listar"),
    path("livros/novo/", views.livro_criar, name="livro_criar"),
    path("livros/<int:pk>/editar/", views.livro_editar, name="livro_editar"),
    path("livros/<int:pk>/excluir/", views.livro_excluir, name="livro_excluir"),
]
