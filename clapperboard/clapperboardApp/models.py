from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from ckeditor.fields import RichTextField

# Create your models here.

#modelo de Avatar 
class Avatar(models.Model):
    
    usuario = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatar/', blank=True)

class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='peliculas', blank=True, null=True)
    fecha_publicacion = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, editable=False)
    
    class Meta:
        ordering = ["-fecha_publicacion"]
    
    def __str__(self):
        return self.titulo
    
class Serie(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='series', blank=True)
    fecha_publicacion = models.DateField(auto_now_add=True)
    # usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Juego(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='juegos', blank=True)
    fecha_publicacion = models.DateField(auto_now_add=True)
    
class Musica(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='musica', blank=True)
    fecha_publicacion = models.DateField(auto_now_add=True)

class Comentario(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    mensaje = models.TextField(max_length=500, blank=True, null=True)
    actualizado = models.DateTimeField(auto_now=True)
    creado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-creado']
    
