from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index.as_view(), name='index'),
    path("movies/", views.movie_list, name="movies"),
    path("songs/", views.song_list, name="songs"),
    #path("hello/<name>", views.hello_there, name="hello_there"),
]