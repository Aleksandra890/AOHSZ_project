from django.shortcuts import render
from .models import New, SME
from .forms import NewtForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news(request):
    articles = New.objects.order_by('data')
    return render(request, 'news/news.html', {'articles': articles})

class NewsDetailView(DetailView):
    model = New
    template_name = 'news/detailnew.html'
    context_object_name = 'post'

class NewsUpdate(UpdateView):
     model = New
     template_name = 'news/add.html'
     fields = ['title', 'text1', 'image', 'fultext', 'data']


class NewsDelete(DeleteView):
     model = New
     success_url = '/#catalog'
     template_name = 'news/delnews.html'


def sme(request):
    chanel = SME.objects.order_by('data1')
    return render(request, 'news/sme.html', {'chanel': chanel})

def add(request):
    error = ''
    if request.method == 'POST':
        form = NewtForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма заполнена не верно!'
    form = NewtForm()
    dat = {
        'form': form,
        'error': error
    }

    return render(request, 'news/add.html', dat)
