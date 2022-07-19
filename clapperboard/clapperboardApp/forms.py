from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class UserRegisterForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña",  widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields= ['username', 'first_name', 'last_name', 'email', 'password1', 'password2'] 
        # help_texts= {k:"" for k in fields}
               
class UserEditForm(UserCreationForm):
    
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    
    email= forms.EmailField(label="Email")
    password1: forms.CharField(label="Contraseña",  widget=forms.PasswordInput, required=False)
    password2: forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)
    
    
    class Meta:
        model = User
        fields= ['first_name', 'last_name', 'email', 'password1', 'password2']
        
class AvatarForm(forms.Form):
     
    imagen = forms.ImageField(label="Imagen")
    
    class Meta:
        model = Avatar
        fields = ['imagen']

class NuevaPelicula(forms.Form):
    titulo = forms.CharField(label="Título")
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea)
    imagen = forms.ImageField(label="Imagen")
    fecha_publicacion = forms.DateField(label="Fecha de publicación")
    #usuario = forms.CharField(label="Usuario")
    
    class Meta:
        model = Pelicula
        fields = ['titulo', 'descripcion', 'imagen', 'fecha_publicacion']

class NuevaSerie(forms.Form):
    titulo = forms.CharField(label="Titulo")
    descripcion = forms.CharField(label="Descripcion")
    imagen = forms.ImageField(label="Imagen")
    fecha_publicacion = forms.DateField(label="Fecha de publicacion")
    usuario = forms.CharField(label="Usuario")
    
    class Meta:
        model = Serie
        fields = ['titulo', 'descripcion', 'imagen', 'fecha_publicacion', 'usuario']

class NuevaJuego(forms.Form):
    titulo = forms.CharField(label="Titulo")
    descripcion = forms.CharField(label="Descripcion")
    imagen = forms.ImageField(label="Imagen")
    fecha_publicacion = forms.DateField(label="Fecha de publicacion")
    usuario = forms.CharField(label="Usuario")
    
    class Meta:
        model = Juego
        fields = ['titulo', 'descripcion', 'imagen', 'fecha_publicacion', 'usuario']

class NuevaMusica(forms.Form):
    titulo = forms.CharField(label="Titulo")
    descripcion = forms.CharField(label="Descripcion")
    imagen = forms.ImageField(label="Imagen")
    fecha_publicacion = forms.DateField(label="Fecha de publicacion")
    usuario = forms.CharField(label="Usuario")
    
    class Meta:
        model = Musica
        fields = ['titulo', 'descripcion', 'imagen', 'fecha_publicacion', 'usuario']

class NuevaComentario(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    mensaje = forms.CharField(max_length=300, required=True, widget=forms.Textarea)

        