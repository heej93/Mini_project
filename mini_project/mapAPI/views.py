from django.shortcuts import render, redirect, get_object_or_404


def main_test(request):

    return render(request, 'mapAPI/main_v2.5.html')


def filter(request):

    return render(request, 'mapAPI/filter.html')
