from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def string1(request):
    return HttpResponse("<h1>task one accomplished!!!!</h1>")

def string2(request):
    return HttpResponse("<h1>task two accomplished!!!!</h1>")
