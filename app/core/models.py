from django.db import models

# Create your models here.

class Teste(models.Model):
    mensagem = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
