from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    mensagem = models.TextField()

class User(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.nome