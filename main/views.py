from django.http.response import HttpResponse
from django.shortcuts import render

def index (request):
    data = {
        'title':'Главная страница',
        'values': ['some', 'hello', '123']
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def profile(request):
    return HttpResponse("<h4>Профиль</h4>")

def test(request):
    return HttpResponse("<h4>Test</h4>")
