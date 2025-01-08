from .forms import UserLoginForm, UserRegistrationForm
from django.http import HttpResponseRedirect  # Usado para redirecionar o usuário para uma nova URL
from django.shortcuts import render, redirect  # 'render' para renderizar templates e 'redirect' para redirecionar o usuário
from main.bd_config import conecta_no_banco_de_dados  # Função personalizada para conectar-se ao banco de dados
from .forms import ContatoForm  # Importa o formulário personalizado 'ContatoForm' para manipulação de dados do usuário
from django.shortcuts import render  # Usado para renderizar templates HTML com dados contextuais
from django.contrib.auth import authenticate, login, logout  # Funções de autenticação para autenticar, logar e deslogar usuários
from django.contrib.auth.models import User  # Modelo de usuário padrão do Django, para criação e manipulação de usuários
#from django.contrib.auth.decorators import login_required  # Para proteger views que exigem um usuário autenticado (comentado)
from django.views.decorators.csrf import csrf_protect  # Ativa a proteção CSRF para uma view específica
from django.contrib.auth.decorators import login_required  # Decorator que exige que o usuário esteja autenticado para acessar a view
from django.contrib.auth.mixins import LoginRequiredMixin  # Mixin para garantir que apenas usuários autenticados acessem views baseadas em classe
from django.shortcuts import render, redirect  # 'render' para templates e 'redirect' para redirecionamentos de URL
from django.http import HttpResponseBadRequest  # Retorna uma resposta HTTP com erro 400 (Bad Request)
from django.db import transaction  # Usado para controlar transações de banco de dados (commit/rollback)
from django.http import HttpResponse, JsonResponse  # 'HttpResponse' para resposta genérica e 'JsonResponse' para respostas JSON
from django.contrib import messages  # Usado para mostrar mensagens de feedback ao usuário, como sucesso ou erro








def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def cursos(request):
    return render(request, 'cursos.html')

def contato(request):
    return render(request, 'contato.html')

def login(request):
     request.method == 'POST'
     email = request.post.get('email')
     senha = request.post.get('senha')
     if not all (email, senha):
         return render (request, 'login.html')
     
     bd = conecta_no_banco_de_dados()
     cursor = bd.cursor()
     cursor.execute(
         """SELECT * FROM usuarios
            WHERE email = %s AND senha = %s;""", 
            (email, senha,))
     
     cursor.close()

     return render (request, 'login.html')


    # return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

def matriculas(request):
    return render(request, 'matriculas.html')

def programacao(request):
    return render(request, 'programacao.html')

def marketing(request):
    return render(request, 'marketing.html')

def design(request):
    return render(request, 'design.html')