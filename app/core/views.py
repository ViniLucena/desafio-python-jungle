#from django.shortcuts import render
from django.http import HttpResponse
from .models import Teste

# Create your views here.

def index(request):
    Teste.objects.create(mensagem="Integração Django + Supabase concluída")
    quantidade = Teste.objects.count()
    return HttpResponse(f"<h1>Desafio do Zé</h1> <p>Conectado ao Supabase (PostgreSQL). Total de registros no banco: {quantidade}</p>")