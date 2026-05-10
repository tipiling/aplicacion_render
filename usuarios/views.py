from django.shortcuts import render
from .forms import UsuarioForm
from .models import Usuario

def registro_usuario(request):
    mensaje = ""
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "Usuario registrado correctamente"
    else:
        form = UsuarioForm()

    return render(request, "formulario.html", {"form": form, "mensaje": mensaje})

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "lista_usuarios.html", {"usuarios": usuarios})
