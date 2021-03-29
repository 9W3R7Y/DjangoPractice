from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def index(request):
    return HttpResponse("Index")


def RenderTemplateExample(request):
    context = {'text': "こんTextはContextとして受け渡されます"}
    return render(request, 'hoge/huga.html', context)


def PathConverterExample(request, num):
    return HttpResponse(num)


def FormExample(request):
    return render(request, 'hoge/form.html')


def SubmitExample(request):
    form_value = request.POST['form_value']
    HttpResponseRedirect(form_value)

