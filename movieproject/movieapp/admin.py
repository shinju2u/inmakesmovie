from django.contrib import admin
from .models import  Movie
from .forms import  MovieForm


# Register your models here.
admin.site.register(Movie)