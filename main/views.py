from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def slid(request):
    return render(request, 'main/slider.html')
