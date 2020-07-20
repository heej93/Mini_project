from django.shortcuts import render
from django.http import HttpResponse

def signMain(request):
    return HttpResponse('<h1>Main</h1>')
