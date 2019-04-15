import json
import requests
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from omdmain.forms import UserRegistrationForm
from omdmain.models import Movies

from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView



class index(TemplateView):
    template_name = 'index.html'

class home(TemplateView):
    template_name = 'home.html'

class movies(TemplateView):
    template_name = 'movies.html'

class save_movie(View):
    def post(self, request, *args, **kwargs):
        user = request.user

        data = json.loads(request.body)
        movie_id = data['imdbId']
        title = data['titleMovie']
        release = data['releaseMovie']
        runtime = data['runtimeMovie']
        actors = data['actorsMovie']
        boxoffice = data['boxofficeMovie']

        try:
            Movies.objects.get(movie_id=movie_id, user=user)
        except ObjectDoesNotExist:
            Movies.objects.create(movie_id=movie_id, title=title, release=release,
                               runtime=runtime, actors=actors, boxoffice=boxoffice,user=user)
        else:
            return HttpResponse(400) # user should be know what doing wrong :/
        return HttpResponse(201)


class saved_movies(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        user_movies = Movies.objects.filter(user=user)
        movies_list = {
            "user_movies": user_movies
        }
        return render(request, "saved_movies.html", movies_list)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password1']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.error(request, "Invalid form!")
                return HttpResponseRedirect(reverse_lazy('omdmain:register'))
    else:
        form = UserRegistrationForm
    return render(request, 'registration/register.html', {'form': form})