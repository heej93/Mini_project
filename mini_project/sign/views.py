from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request, HttpResponseRedirect
from django.urls import reverse
from .models import User

# 로그인
def login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        print(user_id, user_pw)
        u = User.objects.get(user_id=user_id)
        print(u)
        try:
            u = User.objects.get(user_id=user_id)
            print(u)

            if user_pw == User.objects.get(user_id=user_id).user_pw:
                user = User.objects.get(user_id=user_id)
                request.session['user_id'] = user_id
                print(user)
                return render(request, 'sign/join.html',{'user':user})
            else :
                return HttpResponseRedirect('/sign/join/')
        except :
            print('except')
            return HttpResponseRedirect('/sign/join/')
    else :
        return HttpResponseRedirect('/sign/join/')
# 로그아웃
def logout(request):
    request.session.modified = True
    del request.session['user_id']
    return HttpResponseRedirect('/sign/join/')

# 회원가입
def join(request):
    return render(request, 'sign/join.html')

def join_post(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        user_email = request.POST.get('user_email')
        user_dog = request.POST.get('user_dog')
        User.objects.create(user_id=user_id,user_pw=user_pw, user_email=user_email, user_dog=user_dog)
        return HttpResponseRedirect('/sign/join/')
    else:
        return HttpResponseRedirect('/sign/join/')

def user_modi(request):
    return 
    # user_id = request.GET.get('user_id')
    # user_pw = request.GET.get('user_pw')
    # user_email = request.GET.get('user_email')
    # user_dog = request.GET.get('user_dog')
    # user = User.objects.get(user_id = request.session['user_id'])
    # user.user_id = user_id
    # user.user_pw = user_pw
    # user.user_email = user_email
    # user.user_dog = user_dog
    # user.save()
    # request.session['user_id'] = user_id
    # return render(request, 'sign/join.html', {'user' : user})
        


    