from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse


def index(request):
    return HttpResponse("Index")


def RenderTemplateExample(request):
    context = {'text': "こんTextはContextとして受け渡されます"}
    return render(request, 'hoge/huga.html', context)


def PathConverterExample(request, num):
    return HttpResponse(num)


def FormExample(request):
    return render(request, 'hoge/form.html')


@csrf_protect
def SubmitExample(request):
    form_value = request.POST['form_value']
    return HttpResponseRedirect(reverse('hoge:submitted', kwargs={'form_value': form_value}))


def SubmittedExample(request, form_value):
    return HttpResponse(form_value)
