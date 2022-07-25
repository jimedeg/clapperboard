# Clapperboard 

## Descripción
Landing page informativa de películas, series. En la cual te podes loguear, tener un perfil con tus datos personales  
e imagen de perfil. A su vez brinda información de donde podes ver cada peli o serie.  

## Instalación
1- En Github en code copiamos el https:
![Clonar Carpeta Clapperboard](https://user-images.githubusercontent.com/105326853/180692615-dd4fea83-9403-4625-8302-abb4850d5335.jpg)  
  
2- En nuestra terminal elegimos donde clonar la carpeta usando "git clone" y pegamos el link HTTPS que copiamos.  
  `git clone https://github.com/jimedeg/clapperboard.git`  
    
3-Con github desktop:  
![Clonar con Github D Clapper](https://user-images.githubusercontent.com/105326853/180693044-24850151-1335-413e-bb2a-9c48323ef9a9.jpg)  
  
4- Elegimos donde clonar la carpeta.  
   
5- En la carpeta abrimos la consola:  
![abrir consola](https://user-images.githubusercontent.com/105326853/180693418-4b4ae206-9f47-445a-83c3-2a94a5a1c9c8.jpg)  
  
6- Hacemos las migraciones con:  
  `python manage.py makemigrations`  
  `python manage.py migrate`  
     
7- Lanzamos el servidor con:  
  `python manage.py runserver`  

## Panel de administrador  
1- Crear usuario administrador  

 `python manage.py createsuperuser`  

## Dependencias Usadas  
-[Ckeditor](https://django-ckeditor.readthedocs.io/en/latest/#installation "Ckeditor"): lo usamos para que en el formulario de agregar descripciones el texto sea mas enriquecido con estilos.  
-[Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html "Crispy Forms"): lo usamos para mejorar todos lo formularios del proyecto.  
-[ColorField](https://pypi.org/project/django-colorfield/ "ColorField" ): lo usamos para personalizar el panel de administración.  
-[Admin Interface](https://pypi.org/project/django-admin-interface/ "Admin Interface" ): lo usamos para personalizar el panel de administración.

## Creadores  
-Mi nombre es Ignacio Iraola , soy uno de los creadores del proyecto, mi tarea fue realizar el modelo Series y todo lo que el despliega.  


-Mi nombre es Jimena Anahí Degiorgi, soy una de las creadoras de este proyecto, mi tarea fue realizar, el login, logout,  
editar perfil, agregar avatar, como asi tambien crear el modelo Peliculas y todo lo que ella despliega. El Readme y los test, como así tambien la sección de comentarios en la pagina.

 [Linkedin](https://www.linkedin.com/in/jimena-anahí-degiorgi/ "Linkedin" )
