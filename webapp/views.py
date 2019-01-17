from django.http import HttpRequest
from django.shortcuts import render, render_to_response


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def view(request, views):
    return render(request, '%s.html' % (views))


def directory(request, directory, views):
    return render(request, '%s/%s.html' % (directory, views))
