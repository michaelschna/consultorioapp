from django.shortcuts import render

# Create your views here.

def index(request, plantilla="index.html"):
    return render(request, plantilla)



