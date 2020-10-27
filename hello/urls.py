from django.urls import path
from . import views

urlpatterns = [
    #path("", views.home, name="home"),
    path("", views.Index.as_view(), name='index'),
    #path("hello/<name>", views.hello_there, name="hello_there"),
]