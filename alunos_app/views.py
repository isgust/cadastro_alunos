from django.shortcuts import render, redirect
from .forms import AlunoForm

# Create your views here.
def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'alunos_app/cadastro_sucesso.html')
    else:
        form = AlunoForm()
    return render(request, 'alunos_app/cadastrar_aluno.html', {'form': form})        