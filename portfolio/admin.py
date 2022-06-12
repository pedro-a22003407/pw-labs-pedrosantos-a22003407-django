from django.contrib import admin

# Register your models here.
from .models import Post, PontuacaoQuizz
from .models import *

admin.site.register(Post)
admin.site.register(PontuacaoQuizz)
admin.site.register(Cadeira)
admin.site.register(Professor)
admin.site.register(Linguagem)
admin.site.register(Projeto)
admin.site.register(TFC)
