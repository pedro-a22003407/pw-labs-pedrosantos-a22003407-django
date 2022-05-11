from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from matplotlib import pyplot as plt

import datetime

from portfolio.forms import PostForm
from portfolio.models import Post, PontuacaoQuizz


def layout_view(request):
    return render(request, 'portfolio/layout.html')


def home_view(request):
    return render(request, 'portfolio/home.html')


def apresentacao_view(request):
    return render(request, 'portfolio/apresentacao.html')


def formacao_view(request):
    return render(request, 'portfolio/formacao.html')


def projetos_view(request):
    return render(request, 'portfolio/projetos.html')


def competencias_view(request):
    return render(request, 'portfolio/competencias.html')


def blog_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {
        'posts': Post.objects.all(),
        'form': form
    }
    return render(request, 'portfolio/blog.html', context)


def index_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']

    context = {
        'hora': agora.hour,
        'local': local,
        'topicos': topicos,
    }

    return render(request, 'portfolio/home.html', context)


def licenciatura_view(request):
    return render(request, 'portfolio/licenciatura.html')


def heroPage_view(request):
    return render(request, 'portfolio/heroPage.html')


def quizz_view(request):
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontuacao=p)
        r.save()
        desenha_grafico_resultados()

    return render(request, 'portfolio/quizz.html')


def pontuacao_quizz(request):
    pontuacao = 0
    if request.POST['pergunta1'] == "margem":
        pontuacao += 1

    if request.POST['pergunta2'] == "Css3":
        pontuacao += 1

    if request.POST['pergunta3'] == "margem":
        pontuacao += 1

    return pontuacao


def desenha_grafico_resultados():
    participantes = sorted(PontuacaoQuizz.objects.all(), key=lambda t: t.pontuacao)

    nomes = []
    pontuacoes = []

    for pt in participantes:
        nomes.append(pt.nome)
        pontuacoes.append(pt.pontuacao)

    nomes.reverse()
    pontuacoes.reverse()
    plt.barh(nomes, pontuacoes)
    plt.savefig("portfolio/static/portfolio/images/grafico.png", bbox_inches='tight')
