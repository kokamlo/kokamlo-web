from django.shortcuts import render
from django.http import HttpResponse as hp
from .models import Proj

# Create your views here.
def home(request):
    projects = Proj.objects.all()
    return render( request , 'porto/home.html' , {'projects':projects})
