from django.shortcuts import render, redirect
from .forms import diarista_form
from .models import Diaristas

# Create your views here.

#Função para cadastrar as diaristas
def cadastrar_diarista(request):
    if request.method =="POST":
        form_diarista = diarista_form.DiaristaForm(request.POST, request.FILES)
        if form_diarista.is_valid():
            form_diarista.save()
            return redirect('listar_diaristas')
    else:
        form_diarista = diarista_form.DiaristaForm()
    return render(request, 'form_diarista.html', {'form_diarista' : form_diarista})

#Função para listar as diaristas do banco de dados
def listar_diaristas(request):
    diaristas = Diaristas.objects.all()
    return render(request, 'lista_diaristas.html', {'diaristas': diaristas})

#Função para editar as diaristas
def editar_diarista(request, diaristas_id):
    diarista = Diaristas.object.get(id=diaristas_id)
    form_diarista = diarista_form.DiaristaForm(request.POST or None, instance=diarista)
    if form_diarista.is_valid():
        form_diarista.save()
        return redirect('listar_diaristas')
    return render(request, 'form_diarista.html', {'form_diarista': form_diarista})