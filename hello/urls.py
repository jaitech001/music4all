from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path("", views.Index.as_view(), name='index'),
    path("movies/", views.movie_list, name="movies"),
    path("songs/", views.song_list, name="songs"),
    path("singers/", views.singer_list, name="singers"),
]