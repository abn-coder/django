from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index/index.html", {'title': "Home title"})


def explore(request):
    return render(request, "index/explore.html",  {'title': "News title"})


def explore_inner(request, slug):
    return render(request, "index/explore_inner.html",  {'title': "Events title", 'slug': slug})

def about(request):
    return render(request, "index/about.html",  {'title': "News title"})


def faq(request):
    return render(request, "index/faq.html",  {'title': "News title"})




