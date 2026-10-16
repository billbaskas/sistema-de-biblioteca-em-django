from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AutorForm, LivroForm
from .models import Autor, Livro


def home(request):
    contexto = {
        "total_autores": Autor.objects.count(),
        "total_livros": Livro.objects.count(),
    }
    return render(request, "biblioteca/home.html", contexto)


# ---------------------------- AUTORES ----------------------------

def autor_listar(request):  # READ (lista)
    autores = Autor.objects.all()
    return render(request, "biblioteca/autor_lista.html", {"autores": autores})


def autor_detalhe(request, pk):  # READ (detalhe)
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, "biblioteca/autor_detalhe.html", {"autor": autor})


def autor_criar(request):  # CREATE
    form = AutorForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Autor cadastrado com sucesso!")
        return redirect("autor_listar")
    return render(
        request, "biblioteca/form.html", {"form": form, "titulo": "Novo autor"}
    )


def autor_editar(request, pk):  # UPDATE
    autor = get_object_or_404(Autor, pk=pk)
    form = AutorForm(request.POST or None, instance=autor)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Autor atualizado com sucesso!")
        return redirect("autor_listar")
    return render(
        request, "biblioteca/form.html", {"form": form, "titulo": "Editar autor"}
    )


def autor_excluir(request, pk):  # DELETE
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == "POST":
        autor.delete()
        messages.success(request, "Autor excluído com sucesso!")
        return redirect("autor_listar")
    return render(
        request,
        "biblioteca/confirmar_exclusao.html",
        {"objeto": autor, "voltar": "autor_listar",
         "aviso": "Todos os livros deste autor também serão excluídos."},
    )


# ---------------------------- LIVROS ----------------------------

def livro_listar(request):
    livros = Livro.objects.select_related("autor")
    return render(request, "biblioteca/livro_lista.html", {"livros": livros})


def livro_criar(request):
    if not Autor.objects.exists():
        messages.warning(request, "Cadastre um autor antes de cadastrar livros.")
        return redirect("autor_criar")
    form = LivroForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Livro cadastrado com sucesso!")
        return redirect("livro_listar")
    return render(
        request, "biblioteca/form.html", {"form": form, "titulo": "Novo livro"}
    )


def livro_editar(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    form = LivroForm(request.POST or None, instance=livro)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Livro atualizado com sucesso!")
        return redirect("livro_listar")
    return render(
        request, "biblioteca/form.html", {"form": form, "titulo": "Editar livro"}
    )


def livro_excluir(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        livro.delete()
        messages.success(request, "Livro excluído com sucesso!")
        return redirect("livro_listar")
    return render(
        request,
        "biblioteca/confirmar_exclusao.html",
        {"objeto": livro, "voltar": "livro_listar", "aviso": ""},
    )
