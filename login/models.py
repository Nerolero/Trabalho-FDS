from django.db import models

# Usuário individual:
# cadastro: e-mail, senha, nome.

# objetivo:
# Nome, descrição, estar concluído

# Subtarefa:
# Nome, descrição, estar concluído

class Usuario(models.Model):
    Nome = models.CharField(max_length=100, unique=True)
    E_mail = models.EmailField(unique=True)
    Senha = models.CharField(max_length=20)

    def __str__(self):
        return self.Nome



