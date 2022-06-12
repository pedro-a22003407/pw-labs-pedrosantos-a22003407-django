from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from matplotlib import pyplot as plt

import datetime

from portfolio.forms import PostForm, CadeiraForm, ProjetoForm
from portfolio.models import Post, PontuacaoQuizz, Cadeira, Projeto, TFC


def layout_view(request):
    return render(request, 'portfolio/layout.html')


def home_view(request):
    return render(request, 'portfolio/home.html')


def apresentacao_view(request):
    return render(request, 'portfolio/apresentacao.html')


def formacao_view(request):
    return render(request, 'portfolio/formacao.html')


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


def projetos_view(request):
    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))
    context = {'projetos': Projeto.objects.all, 'form': form}
    return render(request, 'portfolio/projetos.html', context)


def licenciatura_view(request):
    form = CadeiraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))
    context = {'cadeiras': Cadeira.objects.all, 'form': form}
    return render(request, 'portfolio/licenciatura.html', context)


def heroPage_view(request):
    return render(request, 'portfolio/heroPage.html')


def contact_view(request):
    return render(request, 'portfolio/contact.html')


def tempo_view(request):
    return render(request, 'portfolio/tempo.html')


def TFC_view(request):
    TFCS = TFC.objects.all()
    context = {'TFCS': TFCS}
    return render(request, 'portfolio/TFC.html', context)


def TFC2_view(request, TFC_ID):
    TFC2 = TFC.objects.get(pk=TFC_ID)
    context = {'TFC': TFC2}
    return render(request, 'portfolio/TFC2.html', context)


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


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:heroPage'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas.'
            })

    return render(request, 'portfolio/login.html')


def logout_view(request):
    logout(request)

    return render(request, 'portfolio/login.html', {
        'message': 'Foi desconetado.'
    })
