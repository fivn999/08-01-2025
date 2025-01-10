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
    request.session['usuario_id'] = ""

    # Se for uma solicitação POST, valida o login
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        # Verifique se o formulário foi validado corretamente
        if form.is_valid():
            # Extrair as credenciais do formulário
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            # Conectar ao banco de dados
            bd = conecta_no_banco_de_dados()

            # Verificar as credenciais no banco de dados
            cursor = bd.cursor()
            cursor.execute("""
                        SELECT *
                        FROM usuarios
                        WHERE email = %s AND senha = %s;
                    """, (email, senha))
            usuario = cursor.fetchone()
            cursor.close()
            bd.close()

            # Se o usuário for encontrado
            if usuario:
                request.session['usuario_id'] = usuario[0]  # Salva o ID do usuário na sessão
                return redirect('index')  # Redireciona para a página inicial

            else:
                # Se não encontrar o usuário, exibe uma mensagem de erro
                mensagem_erro = 'Email ou senha inválidos.'
                return render(request, 'login.html', {'form': form, 'mensagem_erro': mensagem_erro})

    else:
        # Caso contrário, cria um formulário vazio
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})

def registro(request):
    request.session['usuario_id'] = ""

    # Se for uma solicitação POST, valida o login
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        # Verifique se o formulário foi validado corretamente
        if form.is_valid():
            # Extrair as credenciais do formulário
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            # Conectar ao banco de dados
            bd = conecta_no_banco_de_dados()
            cursor = bd.cursor()
            sql = (
                """
                INSERT INTO usuarios
                SET nome = %s, email = %s, senha = %s;
                """
            )
            values = (nome, email, senha)
            cursor.execute(sql, values)
            bd.commit()  
            cursor.close()
            bd.close()


            return redirect('/')
          

    else:
        # Caso contrário, cria um formulário vazio
        form = UserRegistrationForm()

    return render(request, 'registro.html', {'form': form})

def editarusuario(request,id):
    if not request.session.get('usuario_id'):
        return redirect('/')
    else:
        id_usuario = id
        bd = conecta_no_banco_de_dados()
        cursor = bd.cursor()
        cursor.execute("""
            SELECT id, nome, email
            FROM usuarios
            WHERE id = %s;
        """, (id,))
        dados_usuario = cursor.fetchone()
        cursor.close()
        bd.close()
        if request.method == 'POST':
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            senha = request.POST.get('senha')    
            if not all([nome, email, senha]):
                return render(request, 'index.html')
            bd = conecta_no_banco_de_dados()
            cursor = bd.cursor()
            sql = (
                """
                UPDATE usuarios
                SET nome = %s, email = %s, senha = %s
                WHERE id = %s;
                """
            )
            values = (nome, email, senha, id)
            cursor.execute(sql, values)
            bd.commit()  # Assumindo que você tenha gerenciamento de transações
            cursor.close()
            bd.close()

            # Redirecione para a página de sucesso ou exiba a mensagem de confirmação
            return redirect('index')     

        # Exiba o formulário (assumindo lógica de renderização)
        return render(request, 'editarusuario.html',{'id': id_usuario})

def matriculas(request):
    return render(request, 'matriculas.html')


def programacao(request):
    return render(request, 'programacao.html')

def marketing(request):
    return render(request, 'marketing.html')

def design(request):
    return render(request, 'design.html')