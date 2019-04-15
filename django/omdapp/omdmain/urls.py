from django.conf.urls import url, include
from . import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import path

app_name = 'omdmain'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('home/', views.home.as_view(), name='home'),
    path('movies/', views.movies.as_view(), name='movies'),
    path('save_movie/', views.save_movie.as_view(), name='save_movie'),
    path('saved_movies/', views.saved_movies.as_view(), name='saved_movies'),
    path('', views.index.as_view())
]
