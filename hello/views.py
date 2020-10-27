import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
class Index(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)

# def home(request):
#     return HttpResponse("Hello, This is a home page !")

# def hello_there(request, name):
#     now = datetime.now()
#     formatted_now = now.strftime("%A, %d %B, %Y at %X")

#     # Filter the name argument to letters only using regular expressions. URL arguments
#     # can contain arbitrary text, so we restrict to safe characters only.
#     match_object = re.match("[a-zA-Z]+", name)

#     if match_object:
#         clean_name = match_object.group(0)
#     else:
#         clean_name = "Friend"

#     content = "Hello there, " + clean_name + "! It's " + formatted_now
#     return HttpResponse(content)