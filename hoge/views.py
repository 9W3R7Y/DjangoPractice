from django.http import HttpResponse
from django.shortcuts import render


def RenderTemplateExample(request):
    context = {'text': "こんTextはContextとして受け渡されます"}
    return render(request, 'hoge/huga.html', context)


def index(request):
    return HttpResponse("Index")


def PathConverterExample(request, num):
    return HttpResponse(num)
