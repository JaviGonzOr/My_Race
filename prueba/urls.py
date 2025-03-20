"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tareas import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static




urlpatterns = [
    path ('admin/', admin.site.urls),
    path ('', views.home, name='home'),
    path ('registro/', views.registro, name='registro'),
    path ('inicio/', views.inicio, name='inicio'), 
    path ('proximamente/', views.proximamente, name='proximamente'), 
    path ('pilotos/', views.pilotos, name='pilotos'), 
    path ('grafico/', views.grafico, name ='grafico'),
    path ('vista_visita/', views.vista_visita, name ='vista_visita'),
    path ('visitas/', views.visitas, name ='visitas'),
    path ('eliminado/', views.eliminado, name ='eliminado'),
    path ('tarea/', views.tarea_pendiente, name = 'tarea'),
    path ('tarea/completada/', views.tarea_completada, name = 'tarea_completada'),
    path ('c_sesion/', views.c_sesion, name = 'c_sesion'),
    path ('i_sesion/', views.i_sesion, name = 'i_sesion'),
    path ('tarea/crear/', views.crear_tarea, name = 'crear_tarea'),
    path ('visitas/crear/', views.crear_visitas, name = 'crear_visitas'),
    path ('vista_tarea/', views.vista_tarea, name = 'vista_tarea'),
    path ('contacto/',views.contacto, name="contacto"),
    path ('tarea/<int:tarea_id>/', views.detalle_tarea, name = 'detalle_tarea'),
    path ('tarea/<int:tarea_id>/completado', views.tarea_completa, name = 'tarea_completa'),
    path ('tarea/<int:tarea_id>/eliminado', views.tarea_eliminada, name = 'tarea_eliminada'),
    path ('clasificacion/', views.clasificacion_campeonato, name='clasificacion'),
    path ('resultados/', views.resultado_carrera, name='resultados'),
    path('video_gallery', views.video_gallery, name='video_gallery'),
    path('upload/', views.upload_video, name='upload_video'),
   

    
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
