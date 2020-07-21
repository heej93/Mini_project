from django.shortcuts import render
import requests


def map_test(request):
    return render(request, 'kakaoAPI/map_test.html')


