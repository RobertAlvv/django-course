from django.shortcuts import render
from apps.blog.models import Post, Category


def index(request):
    posts = Post.objects.filter(state = True)
    return render(request, 'index.html', {"posts": posts})

def generals(request):
    posts = Post.objects.filter(
        state = True, 
        category = Category.objects.get(name = "Generales")
        ) 
    return render(request, 'generals.html', {"posts": posts})

def programming(request):
    posts = Post.objects.filter(
        state = True, 
        category = Category.objects.get(name = "Programacion")
    ) 
    return render(request, 'programming.html', {"posts": posts})

def tutorials(request):
    posts = Post.objects.filter(
        state = True, 
        category = Category.objects.get(name = "Tutoriales")
    ) 
    return render(request, 'tutorials.html', {"posts": posts})

def technology(request):
    posts = Post.objects.filter(
        state = True, 
        category = Category.objects.get(name = "Tecnologia")
    ) 
    return render(request, 'technology.html', {"posts": posts})

def videogame(request):
    posts = Post.objects.filter(
        state = True, 
        category = Category.objects.get(name = "Video Juego")
    ) 
    return render(request, 'videogame.html', {"posts": posts})
