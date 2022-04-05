from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, "apptasklistmng/index.html")

def signin(request):
    return render(request, "apptasklistmng/signin.html")

def signon(request):
    return render(request, "apptasklistmng/signon.html")