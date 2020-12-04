from django.shortcuts import render
from django.http import HttpResponse


def myregistration(request):
    return render(request, 'registration/registration.html')
# Create your views here.
