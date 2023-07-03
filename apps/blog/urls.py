from django.urls import path
from apps.blog.views import index, generals, programming, technology, tutorials, videogame, post_detail

urlpatterns = [
    path("", index, name="index"),
    path("<slug:slug>/post_detail/", post_detail, name="post_detail"),
    path("generals/", generals, name="generals"),
    path("programming/", programming, name="programming"),
    path("technology/", technology, name="technology"),
    path("tutorials/", tutorials, name="tutorials"),
    path("videogame/", videogame, name="videogame"),
]