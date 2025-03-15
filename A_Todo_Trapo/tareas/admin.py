from django.contrib import admin
from .models import Tarea, ImagenTarea, Proveedor, Visitas, Video, Modelo, Piloto, Carrera, ResultadoCarrera, ImagenAvatar


class ImagenTareaAdmin (admin.TabularInline):
    model = ImagenTarea

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['circuito']
    search_fields = ['circuito']
    list_filter = ['circuito']

class ModeloAdmin (admin.ModelAdmin):
    list_display = ['coche']
       

class TareaAdmin (admin.ModelAdmin):
    list_display = ['titulo', 'creacion']
    search_fields = ['titulo']
    list_filter = ['titulo']
    inlines = [ImagenTareaAdmin]

class VisitasAdmin (admin.ModelAdmin):
    list_display = ['titulo', 'visita']
    search_fields = ['titulo']
    list_filter = ['titulo']


    

admin.site.register(Tarea, TareaAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Visitas, VisitasAdmin)
admin.site.register(Modelo, ModeloAdmin)
#admin.site.register(Equipo)
admin.site.register(Piloto)
admin.site.register(Carrera)
admin.site.register(ResultadoCarrera)
admin.site.register(Video)











