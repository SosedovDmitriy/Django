from django.shortcuts import redirect, render
from django.views.generic.edit import DeleteView, UpdateView
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


def news_home(request):
    news = Articles.objects.order_by('title')
    return render(request, 'news/news_home.html', {"news": news})

class NewsDatailView(DetailView):
    model=Articles
    template_name='news/datails_view.html'
    context_object_name='article'

class NewsUpdateView(UpdateView):
    model=Articles
    template_name='news/create.html'
    form_class=ArticlesForm

class NewsDeleteView(DeleteView):
    model=Articles
    success_url='/news'
    template_name='news/news-delete.html'
 


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма введена неверно'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)
