from django import forms
from django.forms import ModelForm
from .models import Post, Cadeira, Projeto


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição do titulo...'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da tarefa...'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'link do post...'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do autor...'}),

        }

        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
            'link': 'Link',
            'autor': 'Autor',
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'link': 'Campo opcional',
        }


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'


class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'
