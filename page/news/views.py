from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.
class HomePostView(ListView):
    model = Post
    template_name = 'home.html'