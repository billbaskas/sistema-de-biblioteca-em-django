from django.contrib import admin

from .models import Autor, Livro

# Admin usado apenas como apoio durante o desenvolvimento
admin.site.register(Autor)
admin.site.register(Livro)
