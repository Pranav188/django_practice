from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("this link works, this is january month")

def func_feb(request):
    return HttpResponse("this is febuary month")