from django import forms
from django.forms import DateTimeInput
from .models import Tarea, Proveedor, Visitas, Modelo, ResultadoCarrera, Video


class ResultadoCarreraForm (forms.ModelForm):
    class Meta:
        model = ResultadoCarrera
        fields = ['piloto', 'miniatura']
        widgets = {
            'piloto': forms.Select(attrs={'class': 'form-control'}),  
            
           
        }

class ModeloForm (forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ['coche']
       


class VisitasForm(forms.ModelForm):
    class Meta:
        model = Visitas
        fields = "__all__"
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control'}),
            'visita': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'ubicacion': forms.URLInput(attrs={'class': 'form-control'})
        }




class ProveedorForm (forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['circuito', 'ficha_tecnica']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video_file']



class FormularioContacto(forms.Form):

    nombre = forms.CharField(label="Nombre", required=True)

    email = forms.CharField(label="Email", required=True)

    contenido = forms.CharField(label="Contenido", widget=forms.Textarea)
