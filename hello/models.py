from django.db import models

# Create your models here.

class Movies(models.Model):
    movie_name = models.CharField(max_length=200)
    year = models.DateTimeField('date released')
    def __str__(self):
        return self.movie_name, self.year


class Songs(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    song = models.CharField(max_length=200)
    singer = models.CharField(max_length=200)
