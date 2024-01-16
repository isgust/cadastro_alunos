from django.urls import path
from .views import cadastrar_aluno
from alunos_app.views import cadastrar_aluno

urlpatterns = [
    path('cadastrar/', cadastrar_aluno, name = 'cadastrar_aluno'),
]
