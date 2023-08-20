from django.shortcuts import render
from .models import Curso, Profesor
from django.http import HttpResponse
from .forms import CursoForm


def crear_curso(request):
    nombre_curso="Programacion Basica"
    comision_curso="999888"
    print("Creando Curso")
    curso=Curso( nombre= nombre_curso, comision= comision_curso)
    curso.save()
    respuesta= f"Curso creado: {curso.nombre} , {curso.comision}"
    return HttpResponse(respuesta)



def listar_cursos(request):
     cursos=Curso.objects.all()
     respuesta=""
     for curso in cursos:
      respuesta+=f"{curso.nombre} , {curso.comision}<br>"
     return HttpResponse(respuesta)   


def inicio(request):
    return render(request,"AppCoder/inicio.html")






def profesores(request):
    profes=Profesor.objects.all()
    return render(request,"AppCoder/profesores.html", {"profes":profes})




def cursos(request):
    if request.method=="POST":
        form= CursoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            comision=info["comision"]
            curso=Curso(nombre=nombre, comision=comision)
            curso.save()
            return render(request, "AppCoder/cursos.html", {"mensaje":"Curso creado"})
        return render(request, "AppCoder/cursos.html", {"mensaje":"Datos Invalidos"})
        
    else:
        listas=Curso.objects.all()
        formulario_curso=CursoForm()
        return render(request,"AppCoder/cursos.html", {"formulario": formulario_curso})







def estudiantes(request):
    return render(request,"AppCoder/estudiantes.html")



def entregables(request):
    return render(request,"AppCoder/entregables.html")            