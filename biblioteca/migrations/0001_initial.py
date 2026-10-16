import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Autor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("nacionalidade", models.CharField(max_length=60)),
            ],
            options={"verbose_name_plural": "autores", "ordering": ["nome"]},
        ),
        migrations.CreateModel(
            name="Livro",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=150)),
                ("ano_publicacao", models.PositiveIntegerField()),
                ("genero", models.CharField(max_length=60)),
                ("autor", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="livros", to="biblioteca.autor")),
            ],
            options={"ordering": ["titulo"]},
        ),
    ]
