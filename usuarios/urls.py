from django.urls import path
from .views import registro_usuario, lista_usuarios

urlpatterns = [
    path('', registro_usuario),
    path('lista/', lista_usuarios, name='lista_usuarios'),
]