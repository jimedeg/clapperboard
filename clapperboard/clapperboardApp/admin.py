from django.contrib import admin

# Register your models here.

from .models import *
class AvatarAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'imagen')
    
class PeliculaAdmin(admin.ModelAdmin):
    list_display= ('titulo', 'subtitulo', 'descripcion', 'fecha_publicacion', 'imagen', 'usuario')

class SerieAdmin(admin.ModelAdmin):
    list_display= ('titulo', 'subtitulo', 'descripcion', 'fecha_publicacion', 'imagen', 'usuario')
    
class ComentarioAdmin(admin.ModelAdmin):
    list_display= ('nombre', 'email', 'mensaje', 'actualizado', 'creado')


admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Avatar, AvatarAdmin)
