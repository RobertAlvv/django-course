from django.urls import path
from apps.blog.views import index, generals, programming, technology, tutorials, videogame

urlpatterns = [
    path("", index, name="index"),
    path("generals/", generals, name="generals"),
    path("programming/", programming, name="programming"),
    path("technology/", technology, name="technology"),
    path("tutorials/", tutorials, name="tutorials"),
    path("videogame/", videogame, name="videogame"),
]