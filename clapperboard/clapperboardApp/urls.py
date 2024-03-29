from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path ('accounts/login', login_request, name= "accounts/login"),
    path ('accounts/register', register_request, name= "accounts/register"),
    path ('accounts/logout', logout_request, name= "accounts/logout"),
    path ('accounts/editar_perfil', editar_perfil, name= "accounts/editar_perfil"),
    path ('accounts/agregar_avatar', agregar_avatar, name= "accounts/agregar_avatar"),
    
    path ('peliculas', peliculas, name= "peliculas"),
    path ('nueva_pelicula', nueva_pelicula, name= "nueva_pelicula"),
    path ('editar_pelicula/<pelicula_id>/', editar_pelicula, name= "editar_pelicula"),
    path ('eliminar_pelicula/<pelicula_id>/', eliminar_pelicula, name= "eliminar_pelicula"),
    path ('peliculas/<pk>/', PeliculaDetalle.as_view(), name= "PeliculaDetalle"),

    path ('series', series, name= "series"),
    path ('nueva_serie', nueva_serie, name= "nueva_serie"),
    path ('editar_serie/<serie_id>/', editar_serie, name= "editar_serie"),
    path ('eliminar_serie/<serie_id>/', eliminar_serie, name= "eliminar_serie"),
    path ('series/<pk>/', SerieDetalle.as_view(), name= "SerieDetalle"),
    
    path('comentarios/', comentarios, name= "comentarios"),
    
    path('about/', nosotros, name= "about"),
    
    
    
    # path ('comentario', comentario, name= "comentario"),

]
