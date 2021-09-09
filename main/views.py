from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return HttpResponse("<h4>Добрый вечер</h4>")

def about(request):
    return HttpResponse("<h4>Обо мне</h4>")

def profile(request):
    return HttpResponse("<h4>Профиль</h4>")

def test(request):
    return HttpResponse("<h4>Test</h4>")
