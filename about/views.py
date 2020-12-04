from django.shortcuts import render
from django.http import HttpResponse


def myabout(request):
    return render(request, 'about/about.html')
# Create your views here.
