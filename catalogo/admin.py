from django.contrib import admin

# Register your models here.

from catalogo.models import Genero, Linguaguem, Autor, Livro, ExemplarLivro

admin.site.register(Genero)
admin.site.register(Linguaguem)
admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(ExemplarLivro)
