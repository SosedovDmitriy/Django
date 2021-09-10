from django.shortcuts import render
from datetime import datetime
from .models import Articles

def news_home(request):
    #p = Articles(title='Dima', anons="HUI", full_text="asdasdasd",date=datetime.now())
    #p.save()
    news=Articles.objects.all()
    print(news)
    return render(request, 'news/news_home.html', {"news":news})
