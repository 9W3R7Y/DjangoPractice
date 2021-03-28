from django.http import HttpResponse
from django.shortcuts import render


def renderTemplate(request):
    context = {'text': "Hello, world."}
    return render(request, 'hoge/huga.html', context)


def index(request):
    return HttpResponse("Hello, world.")


def PathConverterExample(request, num):
    return HttpResponse(num)
