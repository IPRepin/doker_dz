from django.shortcuts import render
from blog.models import Blog


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog.html', {'blogs': blogs})

# Create your views here.
