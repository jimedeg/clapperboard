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
    
    pelicula = Pelicula.objects.all()[:3]
    series = Series.objects.all()[:3]
    
    if request.user.is_authenticated:
        
        try:
            avatar = Avatar.objects.filter(usuario=request.user)
            url = avatar.imagen.url
        except:
            url = "/media/avatar/generica.jpg"
            return render(request, "clapperboardApp/index.html", {"pelicula": pelicula, "series": series, "url": url})
        
        return render(request, "clapperboardApp/index.html", {"pelicula": pelicula, "series": series})
    
    
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

@login_required
def editar_perfil(request):
    
    user = request.user
    
    if request.method == "POST":
        
        form = UserEditForm(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]

            user.save()
            messages.success(request, "Perfil actualizado con éxito!")
            return redirect("inicio")
        
        else:
            messages.error(request, "Error al actualizar el perfil")
            return redirect("editar_perfil")
    
    else:
         form = UserEditForm(initial={"email": user.email, "first_name": user.first_name, "last_name": user.last_name})
    
    return render(request, "clapperboardApp/editar_perfil.html", {"form": form})          
 
@login_required
def agregar_avatar(request):
    
    if request.method == "POST":
        
        form = AvatarForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            user = User.objects.get(username=request.user.username)
            avatar= Avatar(usuario=user, imagen=form.cleaned_data["imagen"])
            avatar.save()
            
            messages.success(request, "Avatar agregado con éxito!")
            
            return redirect("inicio")
        
        else:
            messages.error(request, "Error al agregar el avatar")
            return redirect("agregar_avatar")
    
    else:
        form = AvatarForm()
    
    return render(request, "clapperboardApp/agregar_avatar.html", {"form": form})

