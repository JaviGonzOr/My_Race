from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import Proveedor, VisitasForm, ModeloForm,ResultadoCarreraForm, VideoForm
from .models import Tarea, Proveedor,ImagenTarea, Visitas, Modelo, Piloto, ResultadoCarrera, Video
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.generic import TemplateView
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required




# Create your views here.


def home(request):
    return render(request, 'home.html')


def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return render(request, 'home.html', {
                    'exito': 'Usuario creado con exito'
                })
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'El Usuario ya existe'
                })

        return render(request, 'registro.html', {
            'form': UserCreationForm,
            'error': 'Las Contraseñas no coinciden'
        })


@login_required
def tarea_pendiente(request):
    tareas = Tarea.objects.filter(completado__isnull=True)
    return render(request, 'tarea_pendiente.html', {'tarea': tareas})


@login_required
def tarea_completada(request):
    tareas = Tarea.objects.filter(completado__isnull=True)
    return render(request, 'tarea_completada.html', {'tarea': tareas})


@login_required
def detalle_tarea(request, tarea_id):
    if request.method == 'GET':
        task = get_object_or_404(Tarea, pk=tarea_id)
        form = ResultadoCarreraForm(instance=task)
        return render(request, 'detalle_tarea.html', {'tarea': task, 'form': form})
    else:
        task = get_object_or_404(Tarea, pk=tarea_id)
        form = ResultadoCarreraForm(request.POST, instance=task, files=request.FILES)
        form.save()
        return redirect('tarea')
    

@login_required
def tarea_completa(request, tarea_id):
    task = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)
    if request.method == 'POST':
        task.completado = timezone.now()
        task.save()
        return redirect('tarea')


@login_required
def tarea_eliminada(request, tarea_id):
    task = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)
    if request.method == 'POST':
        task.delete()
        return render(request, 'tarea_completada.html')
    task.delete()
    return render(request, 'eliminado.html')


@login_required
def crear_tarea(request):
    if request.method == 'GET':
        return render(request, 'crear_tarea.html', {
            'form': TareaForm
        })
    else:
        form = TareaForm(request.POST, files=request.FILES)
        new_task = form.save(commit=False)
        new_task.usuario = request.user
        new_task.save()
        return redirect('tarea')
    
@login_required
def crear_visitas(request):
    if request.method == 'GET':
        return render(request, 'crear_visitas.html', {
            'form': VisitasForm
        })
    else:
        form = VisitasForm(request.POST, files=request.FILES)
        new_task = form.save(commit=False)
        new_task.usuario = request.user
        new_task.save()
        return redirect('visitas')


@login_required
def c_sesion(request):
    logout(request)
    return redirect('home')


def i_sesion(request):
    if request.method == 'GET':
        return render(request, 'i_sesion.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'i_sesion.html', {
                'form': AuthenticationForm,
                'error': 'Contraseña o Nombre incorrecto'
            })
        else:
            login(request, user)
            return redirect('inicio')


def grafico(request):
    elementos = ResultadoCarrera.objects.all()
    modelos = ""
    cantidades = ""
    for i in elementos:
        modelos = modelos + "'" + str(i.posicion) + "',"
        cantidades = cantidades + str(i.puntos) + ","

    return render(request, 'grafico.html', {
        'elementos': elementos,
        'modelos': modelos,
        'cantidades': cantidades,
    })


def eliminado(request):
    return render(request, 'eliminado.html')



@login_required
def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Mensaje desde App My TASKS by GonzOr",
                                 "El usuario con nombre {} con email {} ha comentado que:\n\n {}".format(
                                     nombre, email, contenido),
                                 "", ["helice.uno@gmail.com"], reply_to=[email])

            try:
                email.send()

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request, "contacto.html", {'miFormulario': formulario_contacto})


def vista_tarea(request):
    vista_tarea = Tarea.objects.filter(
        usuario = request.user, completado__isnull = True)
    return render(request, "vista_tarea.html", {"vista_tarea": vista_tarea})


def vista_visita(request):
    vista_visita = Visitas.objects.filter(
        usuario = request.user,
        )
    return render(request, "vista_visita.html", {"vista_visita": vista_visita})


def visitas(request):
    events = Visitas.objects.filter(
        usuario = request.user)

    return render(request, 'visitas.html', {'events': events})


    
def inicio(request):
    return render(request, 'inicio.html')


def clasificacion_campeonato(request):

    piloto = Piloto.objects.all().order_by('-puntos', '-victorias', '-podios')
   
    return render(request, 'clasificacion.html', {'pilotos':piloto})


def resultado_carrera(request):
    posicion = ResultadoCarrera.objects.all().order_by('-cat' )

    return render(request, 'resultados.html', {'posiciones':posicion})


def video_gallery(request):
    videos = Video.objects.all()
    return render(request, 'video_gallery.html', {'videos': videos})

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_gallery')
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

def mostrar_tabla(request):
    
    datos = ResultadoCarrera.objects.all()
    return render(request, 'resultados.html', {'datos': datos})