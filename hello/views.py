import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Movies, Songs

# Create your views here.
class Index(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)

def movie_list(request):
    movies = Movies.objects.all()
    # context={
    #     'movies': movies
    # }
    return render(request,"movies.html",{'movies': movies})

def song_list(request):
    songs = Songs.objects.all()
    # context={
    #     'songs':songs
    # }
    return render(request,"songs.html",{'songs': songs})