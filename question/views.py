from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from .forms import Maskform


def myquestion(request):
    if request.method == 'POST':
        form = Maskform(request.POST)
        if form.is_valid():
            form.save()

    form = Maskform()
    context = {'task': form }
    return render (request, 'question/question.html', context )