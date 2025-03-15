from django.db import models
from django.contrib.auth.models import User



# Create your models here.


    
class Proveedor(models.Model):
    circuito = models.CharField(max_length = 100)
    ficha_tecnica = models.FileField(upload_to='Chimeneas', null=True)
        
    def __str__(self):
        return self.circuito
    
class Modelo (models.Model):
    coche = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.coche




class Tarea (models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    configuracion = models.TextField(null=True, blank=True)
    creacion = models.DateTimeField(auto_now_add = True)
    completado= models.DateTimeField(null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    circuito = models.ForeignKey(Proveedor,null=True, on_delete = models.PROTECT)
    coche = models.ForeignKey(Modelo, null=True, on_delete = models.PROTECT)
    
    def __str__(self):
        return self.titulo 
    
class Visitas(models.Model):
    titulo = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    visita = models.DateTimeField(null=True, blank=True)
    ubicacion = models.URLField(null=True, blank=True)
   
    
    
    def __str__(self):
        return self.titulo
    

class ImagenTarea (models.Model):
    imagen = models.FileField (upload_to = "Chimeneas")
    carrera = models.ForeignKey(Tarea, on_delete = models.CASCADE,null=True, related_name='archivos')


#class Equipo(models.Model):
    nombre = models.CharField(max_length=100, null= True, unique=True)
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Piloto(models.Model):
    nombre = models.CharField(max_length=100)
    #equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="pilotos")
    puntos = models.IntegerField(default=0)
    carreras_disputadas = models.IntegerField(default=0)
    victorias = models.IntegerField(default=0)
    v_rapida = models.IntegerField(default=0)
    podios = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='Chimeneas/', null=True)

    def image_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url

    def __str__(self):
        return self.nombre
    

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    circuito = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class ResultadoCarrera(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name="resultados")
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE, related_name="resultados")
    trial = models.IntegerField(null=True)
    cat = models.IntegerField(null=True)
    dragon = models.IntegerField(null=True)
    mount = models.IntegerField(null=True)
    suzuka = models.IntegerField(null=True)
    grand = models.IntegerField(null=True)
    spa = models.IntegerField(null=True)
    kioto = models.IntegerField(null=True)
    lago = models.IntegerField(null=True)
    tokio = models.IntegerField(null=True)
    miniatura = models.ImageField(upload_to='Chimeneas/', null=True)
    foto_circuito = models.ImageField(upload_to='Chimeneas/', null=True)
    

    def image_url(self):
        if self.miniatura and hasattr(self.miniatura, 'url'):
            return self.miniatura.url
    def imagen_url(self):
        if self.foto_circuito and hasattr(self.foto_circuito, 'url'):
            return self.foto_circuito.url



    def __str__(self):
        return f"{self.carrera.nombre} - {self.piloto.nombre}"
    

    

class ImagenAvatar (models.Model):
    avatar = models.FileField (upload_to = "Chimeneas")
    karrera = models.ForeignKey(Piloto, on_delete = models.CASCADE, related_name='archivo')
    

   
class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
