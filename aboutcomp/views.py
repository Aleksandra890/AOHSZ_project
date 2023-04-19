from django.shortcuts import render

def about(request):
    return render(request, 'aboutcomp/about.html')

def manag(request):
    return render(request, 'aboutcomp/manage.html')

def purchas(request):
    return render(request, 'aboutcomp/purchas.html')

def anti_cor(request):
    return render(request, 'aboutcomp/anti_cor.html')

def disclosur(request):
    return render(request, 'aboutcomp/disclosur.html')
