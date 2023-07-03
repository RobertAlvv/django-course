from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

from apps.blog.models import Post, Category


def index(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(state = True)
    
    if queryset:
      
      posts =  Post.objects.filter(
          Q(title__icontains=queryset) | 
          Q(description__icontains= queryset)
      ).distinct()
    
    paginator = Paginator(posts, 2)
    page = request.GET.get("page", 1)
    posts = paginator.get_page(page)
    
    return render(request, 'index.html', {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug = slug)
        
    return render(request, 'post.html', {"post":post})

def generals(request):
    queryset = request.GET.get("buscar")
    
    posts = Post.objects.filter(
        state = True, 
        category = Category.objects.get(name__iexact = "Generales")
        )
    
    if queryset:
      posts = Post.objects.filter(
          Q(title__icontains=queryset) | 
          Q(description__icontains= queryset),
          state= True, 
          category = Category.objects.get(name__iexact = "Generales"), 
        ).distinct()
      
    paginator = Paginator(posts, 2)
    page = request.GET.get("page", 1)
    posts = paginator.get_page(page)
    
    return render(request, 'generals.html', {"posts": posts})

def programming(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        state = True, 
        category = Category.objects.get(name__iexact = "Programacion")
    )
    if queryset:
      posts = Post.objects.filter(
          Q(title__icontains=queryset) | 
          Q(description__icontains= queryset),
          state= True, 
          category = Category.objects.get(name__iexact = "Programacion"), 
        ).distinct()
    
    paginator = Paginator(posts, 2)
    page = request.GET.get("page", 1)
    posts = paginator.get_page(page)
            
    return render(request, 'programming.html', {"posts": posts})

def tutorials(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        state = True, 
        category = Category.objects.get(name__iexact = "Tutoriales")
    )

    if queryset:
      posts = Post.objects.filter(
          Q(title__icontains=queryset) | 
          Q(description__icontains= queryset),
          state= True, 
          category = Category.objects.get(name__iexact = "Tutoriales"), 
        ).distinct()

    paginator = Paginator(posts, 2)
    page = request.GET.get("page", 1)
    posts = paginator.get_page(page)
     
    return render(request, 'tutorials.html', {"posts": posts})

def technology(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        state = True, 
        category = Category.objects.get(name__iexact = "Tecnologia")
    )
    
    if queryset:
      posts = Post.objects.filter(
          Q(title__icontains=queryset) | 
          Q(description__icontains= queryset),
          state= True, 
          category = Category.objects.get(name__iexact = "Tecnologia"), 
        ).distinct()
    
    paginator = Paginator(posts, 2)
    page = request.GET.get("page", 1)
    posts = paginator.get_page(page)
                
    return render(request, 'technology.html', {"posts": posts})

def videogame(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        state = True, 
        category = Category.objects.get(name__iexact = "Video Juegos")
    ) 
    
    if queryset:
      posts = Post.objects.filter(
          Q(title__icontains=queryset) | 
          Q(description__icontains= queryset),
          state= True, 
          category = Category.objects.get(name__iexact = "Video Juegos"), 
        ).distinct() 

    paginator = Paginator(posts, 2)
    page = request.GET.get("page", 1)
    posts = paginator.get_page(page)

    return render(request, 'videogame.html', {"posts": posts})
