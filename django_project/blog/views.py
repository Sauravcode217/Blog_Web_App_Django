from django.shortcuts import render
from django.http import HttpResponse 


# def home(request):
#     return HttpResponse('<h1>Blog Home</h1>')

def home(request):
    return render(request, 'blog/home.html')


# def about(request):
#     return HttpResponse('<h2> Blog About </h1>')

def about(request):
    return render(request, 'blog/about.html')
