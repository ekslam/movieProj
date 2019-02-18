from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movies
from .forms import (MovieModuleForm, RegistrationModelForm)
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def index(request):
    mov = {}
    movies = Movies.objects.all()
    mov['movies'] = movies
    return render(request, 'index.html', mov)

@login_required
def movies_detail(request, movies_id):
    mov = {}
    mov['movies'] = Movies.objects.get(id=movies_id)
    return render(request,'detail.html', mov)

@login_required
def add_movie(request):
    mov = {}
    mov['form'] = MovieModuleForm()
    if request.method == 'POST':
        form = MovieModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/prefMovie/')
        else:
            mov['form'] = form
            render(request,'addMovie.html', mov)
    else:
        return render(request, 'addMovie.html', mov)

@login_required
def update_movie(request, movies_id):
    mov = {}
    movies = Movies.objects.get(id=movies_id)
    if request.method == 'POST':
        form = MovieModuleForm(request.POST, instance=movies)
        if form.is_valid():
            form.save()
            return HttpResponse('Movie Updated')
        else:
            mov['form'] = form
            render(request, 'update.html', mov)
    else:
        mov['form'] = MovieModuleForm(instance=movies)
    return render(request, 'update.html', mov)

def registration(request):
    form = RegistrationModelForm()
    mov = {}
    mov['form'] = form
    if request.method == 'POST':
        form = RegistrationModelForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(request.POST['password'])
            user.save()
            login(request, user)
            return redirect('prefMovie:index')
        else:
            mov['form'] = form
    return render(request, 'registration.html', mov)

def user_login(request):
    mov = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user)
            login(request, user)
            return redirect('prefMovie:index')
    return render(request, 'login.html', mov)


def user_logout(request):
    mov = {}
    logout(request)
    return redirect('prefMovie:index')