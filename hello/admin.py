from django.contrib import admin

# Register your models here.
from .models import Movies
from .models import Songs

admin.site.register(Movies)
admin.site.register(Songs)
