import os
import sys

from  cx_Freeze import setup, Executable

files = ['static', 'Chimeneas','db.sqlite3']

exe = Executable(script = "manage.py", base = "win32GUI")

setup(
    name = "my Tasks by GonzOr",
    version = "1.0",
    descripcion = "Planea, Gestiona y Sigue Todas las Tareas con un Software Flexible. Una Nueva Forma Eficiente y Transparente de Organizar Todas las Tareas de Tu Empresa.",
    autor = "GonzOr Developer",
    opciones = {'build_exe':{'include_files': files}},
    ejecutables =[exe]

)