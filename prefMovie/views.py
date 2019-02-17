from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movies, Users
from .forms import MovieModuleForm, UsersModuleForm
from datetime import datetime

# Create your views here.
def index(request):
    mov = {}
    movies = Movies.objects.all()
    mov['movies'] = movies
    return render(request, 'index.html', mov)

def movies_detail(request, movies_id):
    mov = {}
    mov['movies'] = Movies.objects.get(id=movies_id)
    return render(request,'detail.html', mov)

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
        #question = Question.objects.get(id=question_id)
        mov['form'] = MovieModuleForm(instance=movies)
        #context['q_id'] = question_id
    return render(request, 'update.html', mov)
