from django.shortcuts import render, redirect, get_object_or_404

def map_test(request):
    
    return render(request, 'mapAPI/map_test.html')

def main_test(request):
   
    return render(request, 'mapAPI/main_v2.0.html')



