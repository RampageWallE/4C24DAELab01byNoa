from django.shortcuts import render
from .models import Task
from django.http import HttpResponse

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def sumar(request, a, b):
    suma = a + b
    # return HttpResponse(f'La suma de {a} y {b} es igual a {suma}')
    return render(request, 'tasks/suma.html', {'suma' : suma, 'n1': a, 'n2': b })

def restar(request, a, b):
    resta = a - b
    return render(request, 'tasks/resta.html', {'resta' : resta, 'n1': a, 'n2': b })

def multiplicar(request, a, b):
    multiplicacion = a * b
    return render(request, 'tasks/multiplicacion.html', {'multiplicacion' : multiplicacion, 'n1': a, 'n2': b })

def potencia(request, a, b):
    potencia = a ** b
    return render(request, 'tasks/potencia.html', {'potencia' : potencia, 'n1' : a, 'n2' : b })