from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path ('login', login_request, name= "login"),
    path ('register', register_request, name= "register"),
    path ('logout', logout_request, name= "logout"),
    path ('editar_perfil', editar_perfil, name= "editar_perfil"),
    path ('agregar_avatar', agregar_avatar, name= "agregar_avatar"),
    
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
    
    
    # path ('comentario', comentario, name= "comentario"),

]
