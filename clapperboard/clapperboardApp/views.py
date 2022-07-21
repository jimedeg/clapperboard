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

from django.views.generic.detail import DetailView

# Create your views here.
def inicio(request):
    
    pelicula = Pelicula.objects.all()[:3]
    series = Serie.objects.all()[:3]
    
    if request.user.is_authenticated:
        
        try:
            avatar = Avatar.objects.filter(usuario=request.user)
            url = avatar.imagen.url
        except:
            url = "/media/avatar/generica.jpg"
            return render(request, "clapperboardApp/index.html", {"pelicula": pelicula, "series": series, "url": url})
        
    return render(request, "clapperboardApp/index.html", {"pelicula": pelicula, "series": series})

def login_request(request):
    
    if request.method == "POST":
        
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
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

def peliculas(request):
        
    if request.method == "POST":
        
        buscar = request.POST["buscar"]
        
        if buscar != "":
            pelicula = Pelicula.objects.filter(Q(titulo__icontains=buscar)).values()
            
            return render(request, "clapperboardApp/peliculas.html", {"pelicula": pelicula, "buscar": True, "busqueda":buscar})
    
    # peliculas = list(Pelicula.objects.filter(
    #             titulo= True, 
    #             descripcion = True,).values_list('id', flat=True))
    # principal = random.choice(peliculas)
    # principal = Pelicula.objects.get(id=principal)
    # contexto= {"pelicula": principal}                    
    pelicula = Pelicula.objects.all()
    
    return render(request, "clapperboardApp/peliculas.html", {"pelicula": pelicula, "buscar": False})      
        
@staff_member_required
def nueva_pelicula(request):
    
    if request.method == "POST":
        
        form = NuevaPelicula(request.POST, request.FILES)
        
        if form.is_valid():
            
            info_pelicula = form.cleaned_data
            pelicula = Pelicula(titulo=info_pelicula["titulo"], descripcion=info_pelicula["descripcion"], imagen=info_pelicula["imagen"], fecha_publicacion=info_pelicula["fecha_publicacion"])
            pelicula.save() 
            messages.success(request, "Pelicula agregada con éxito!")
            return redirect("peliculas")
        
        else:
            messages.error(request, "Error al agregar la pelicula")
            return render(request, "clapperboardApp/form_pelicula.html", {"form": form})
    
    else:
        form_vacio = NuevaPelicula()
    
        return render(request, "clapperboardApp/form_pelicula.html", {"form": form_vacio})

@staff_member_required
def editar_pelicula(request, pelicula_id):
    
    pelicula= Pelicula.objects.get(id=pelicula_id)
    
    if request.method == "POST":
        
        form = NuevaPelicula(request.POST, request.FILES)
        
        if form.is_valid():
            
            info_pelicula = form.cleaned_data
            
            pelicula.titulo = info_pelicula["titulo"]
            pelicula.descripcion = info_pelicula["descripcion"]
            pelicula.imagen = info_pelicula["imagen"]
            pelicula.fecha_publicacion = info_pelicula["fecha_publicacion"]
            pelicula.save() 
            messages.success(request, "Pelicula actualizada con éxito!")
            return redirect("peliculas")
        
        else:
            messages.error(request, "Error al actualizar la pelicula")
            return render(request, "clapperboardApp/form_pelicula.html", {"form": form} )
    
    form = NuevaPelicula(initial={"titulo": pelicula.titulo, "descripcion": pelicula.descripcion, "imagen": pelicula.imagen, "fecha_publicacion": pelicula.fecha_publicacion})
       
    return render (request, "clapperboardApp/form_pelicula.html", {"form": form })
    
@staff_member_required
def eliminar_pelicula(request, pelicula_id):
    
    pelicula= Pelicula.objects.get(id=pelicula_id)
    pelicula.delete()
    messages.success(request, "Pelicula eliminada con éxito!")
    return redirect("peliculas")

class PeliculaDetalle(DetailView):
    model = Pelicula
    template_name = "clapperboardApp/pelicula_detalle.html"
    context_object_name = "pelicula"

def series(request):
        
    if request.method == "POST":
        
        buscar = request.POST["buscar"]
        
        if buscar != "":
            serie = Serie.objects.filter(Q(titulo__icontains=buscar)).values()
            
            return render(request, "clapperboardApp/peliculas.html", {"serie": serie, "buscar": True, "busqueda":buscar})
    
            
    serie = Serie.objects.all()
    
    return render(request, "clapperboardApp/peliculas.html", {"pelicula": serie, "buscar": False})      
