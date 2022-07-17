from django.shortcuts import render,redirect
#from django.http import HttpResponse
from django.db.models import Q

from .models import *
from .forms import *

from django.contrib.auth.forms import AuthenticationForm #, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def inicio(request):
    
    return render(request, 'clapperboardApp/index.html')

def login_request(request):
    
    if request.method == "POST":
        
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido {username}!")
                return redirect("inicio")
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
                return redirect("login")

        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect("login")
        
    form = AuthenticationForm()
        
    return render(request, 'clapperboardApp/login.html', {'form': form})

def register_request(request):
    
    if request.method == "POST":
        
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            form.save()
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Usuario creado con éxito!")
                return redirect("inicio")
            else:
                return redirect("login")
            
        password1 = form.data['password1']
        password2 = form.data['password2']
            
        for msg in form.errors.as_data():
            if msg == 'email':
                messages.error(request, "El correo es invalido o ya existe.")
            if msg == 'username':
                messages.error(request, "El nombre de usuario es invalido o ya existe.")
            if msg == 'password2' and password1 == password2:
                messages.error(request, "La contraseña elegida no cumple los requisitos.")
            elif msg == 'password2' and password1 != password2:
                messages.error(request, "Las contraseñas no coinciden.")
                 
        return render(request,"clapperboardApp/register.html",{"form": form})

    form = UserRegisterForm()

    return render(request,"clapperboardApp/register.html",{"form": form})
      
def logout_request(request):
    logout(request)
    messages.success(request, "Sesión cerrada con éxito!")
    return redirect("inicio")
            
       