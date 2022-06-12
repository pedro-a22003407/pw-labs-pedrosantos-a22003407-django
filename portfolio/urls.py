"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.heroPage_view, name='heroPage'),
    path('layout', views.layout_view),
    path('home', views.home_view, name='home'),
    path('contact', views.contact_view, name='contact'),
    path('projetos', views.projetos_view, name='projetos'),
    path('licenciatura', views.licenciatura_view, name='licenciatura'),
    path('heroPage', views.heroPage_view, name='heroPage'),
    path('blog', views.blog_view, name='blog'),
    path('quizz', views.quizz_view, name='quizz'),
    path('login', views.login_view, name='login'),
    path('tempo', views.tempo_view, name='tempo'),
    path('logout', views.logout_view, name='logout'),
    path('TFC', views.TFC_view, name='TFC'),
    path('TFC2/<int:TFC_ID>', views.TFC2_view, name='TFC2'),
]