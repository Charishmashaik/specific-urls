from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def dhoni(request):
    return HttpResponse('<h1>MSD is the best player in the world</h1>')




