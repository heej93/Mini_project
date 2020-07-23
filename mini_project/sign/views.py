from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.forms.models import model_to_dict
from .models import User

# 로그인
def login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        try:
            User.objects.get(user_id=user_id)
            if user_pw == User.objects.get(user_id=user_id).user_pw:
                user = User.objects.get(user_id=user_id)
                request.session['user_id'] = user_id
                print(user)
                return HttpResponseRedirect('/map/main/')
                # return render(request, 'mapAPI/main_v2.0.html', {'user':user})
            else :
                return HttpResponseRedirect('/map/main/')
        except :
            print('except')
            return HttpResponseRedirect('/map/main/')
    else :
        return HttpResponseRedirect('/map/main/')
# 로그아웃
def logout(request):
    request.session.modified = True
    del request.session['user_id']
    return HttpResponseRedirect('/map/main/')

# 회원가입
def join(request):
    return render(request, '/sign/join_post/')

def join_post(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        user_email = request.POST.get('user_email')
        user_dog = request.POST.get('user_dog')
        User.objects.create(user_id=user_id,user_pw=user_pw, user_email=user_email, user_dog=user_dog)
        return HttpResponseRedirect('/map/main/')
    else:
        return HttpResponseRedirect('/map/main/')

def modi_info(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(user_id=request.session['user_id'])
    print(user)

    if request.method == 'POST':
        user.user_id = request.POST.get('user_id')
        user.user_pw = request.POST.get('user_pw')
        user.user_email = request.POST.get('user_email')
        user.user_dog = request.POST.get('user_dog')
        user.save()
        request.session['user_id'] = request.POST.get('user_id')
        return render(request, '/map/main.html',{'user':user})
    
    return JsonResponse(model_to_dict(user), safe=False)

def user_drop(request):
    user = User.objects.get(user_id=request.session['user_id'])
    user.delete()
    request.session.modified = True
    del request.session['user_id']
    return HttpResponseRedirect('/map/main/')
    