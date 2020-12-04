from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Content
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import get_user_model, login, logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import Answerform


def myindex(request):
    return render(request, 'index/index.html')



def mydash(request):
    query = Content.objects.all()
    context ={'qs': query}
    return render(request, 'index/dash.html', context)



def mypage(request, myid):
    if request.method == 'POST':
        form = Answerform(request.POST)
        if form.is_valid():
            form.save()

    form = Answerform()
    query = Content.objects.get(id=myid)
    context = {'content': form, 'qs': query}    
    return render(request, 'index/page.html', context)

def myregister(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = get_user_model().objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            return redirect('index')
    context = {'register':form}
    return render(request,'registration/registration.html', context)


def mylogin(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dash')
    context = { 'log':form}
    return render(request,'index/login.html', context)

def mylogout(request):
    logout(request)
    return redirect('login')


# @login_required(login_url='login')
# def mydash(request):
#     username = request.user.username
#     return render(request,'index/dash.html')


# Create your views here.
