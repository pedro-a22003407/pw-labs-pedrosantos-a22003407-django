from django.contrib import admin

# Register your models here.
from .models import Post, PontuacaoQuizz

admin.site.register(Post)
admin.site.register(PontuacaoQuizz)