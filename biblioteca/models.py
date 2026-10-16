from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=60)

    class Meta:
        ordering = ["nome"]
        verbose_name_plural = "autores"

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    ano_publicacao = models.PositiveIntegerField()
    genero = models.CharField(max_length=60)
    # Relacionamento: um autor possui vários livros
    autor = models.ForeignKey(
        Autor, on_delete=models.CASCADE, related_name="livros"
    )

    class Meta:
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo
