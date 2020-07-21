from django.shortcuts import render

def map_test(request):
    
    return render(request, 'mapAPI/map_test.html')

def main_test(request):

    
    return render(request, 'mapAPI/main_v0.3.html')

