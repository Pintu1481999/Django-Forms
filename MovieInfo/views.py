from django.shortcuts import render
from django.http import HttpResponse
from .models import MovieInfo

# Create your views here.
def index(request):
    # params =  {'Movies': MovieInfo.objects.all()}
    allmovies = MovieInfo.objects.all()
    return render(request, 'index.html', {'movie_list': allmovies})

def AddMovie(request):
    return render(request, 'addmovie.html')

def form_submission(request):

    movie_name = request.POST["movie_name"]
    movie_desc = request.POST["movie_desc"]
    created_date = request.POST["created_date"]
    release_date = request.POST["release_date"]
    file = request.POST["file"]

    movie_info = MovieInfo(movie_name=movie_name, movie_desc=movie_desc, created_date=created_date, release_date=release_date, movie_image=file)

    movie_info.save()
    return render(request, 'addmovie.html')