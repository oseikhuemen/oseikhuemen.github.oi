from django.shortcuts import render
from django.http import HttpResponse


def myschedule(request):
    return render(request, 'schedule/schedule.html')
# Create your views here.
