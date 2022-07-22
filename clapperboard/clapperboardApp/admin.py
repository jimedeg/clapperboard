from django.contrib import admin

# Register your models here.

from .models import *
class PeliculaAdmin(admin.ModelAdmin):
    list_display= ('titulo', 'subtitulo', 'descripcion', 'fecha_publicacion')

class SerieAdmin(admin.ModelAdmin):
    list_display= ('titulo', 'descripcion', 'fecha_publicacion')


admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Avatar)
