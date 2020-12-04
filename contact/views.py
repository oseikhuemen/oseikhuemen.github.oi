from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from .forms import Contactform


def mycontact(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()

    form = Contactform()
    context = {'mutant': form }
    return render (request, 'contact/contact.html', context )
