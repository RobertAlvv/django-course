from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def generals(request):
    return render(request, 'generals.html')

def programming(request):
    return render(request, 'programming.html')

def tutorials(request):
    return render(request, 'tutorials.html')

def technology(request):
    return render(request, 'technology.html')

def videogame(request):
    return render(request, 'videogame.html')
