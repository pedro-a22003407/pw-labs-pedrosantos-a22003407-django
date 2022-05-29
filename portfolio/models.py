from django.db import models


# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    link = models.URLField(blank=True)
    autor = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo[:50]


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=200)
    pontuacao = models.TextField()

    def __str__(self):
        return self.nome[:50]


class Professor(models.Model):
    nome = models.CharField(max_length=20)
    linkLusofona = models.URLField
    linkLinkedin = models.URLField

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.CharField(max_length=255)
    imagem = models.ImageField

    def __str__(self):
        return self.nome


class Linguagem(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Cadeira(models.Model):
    nome = models.CharField(max_length=20)
    ano = models.IntegerField()
    descricao = models.TextField()
    linguagens = models.ManyToManyField(Linguagem)
    docente_teorica = models.ForeignKey(Professor, on_delete=models.CASCADE)
    docentes_praticas = models.ManyToManyField(Professor, related_name='caderias')
    projetos = models.ManyToManyField(Projeto)

    def __str__(self):
        return f"{self.nome} {self.ano}"
