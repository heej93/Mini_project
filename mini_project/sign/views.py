from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.urls import reverse
from .models import User


def join(request):
    return render(request, 'sign/join.html')

def join_post(request):
    user_id = request.POST.get('user_id')
    user_pw = request.POST.get('user_pw')
    user_email = request.POST.get('user_email')
    user_dog = request.POST.get('user_dog')
    User.objects.create(user_id=user_id,user_pw=user_pw, user_email=user_email, user_dog=user_dog)
    return render(request,'sign/join.html')