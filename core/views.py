from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request , 'index.html' , context ,)
def detail(request , slug ):
    posts = Post.objects.get(slug=slug)
    context = {
        'posts' : posts
    }
    return render(request , 'details.html' , context ,)

