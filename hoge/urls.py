from django.urls import path

from . import views

app_name = "hoge"
urlpatterns = [
    path('', views.index, name='index'),
    path('RenderTemplate', views.RenderTemplateExample, name='RenderTemplate'),
    path('<int:num>', views.PathConverterExample, name='PathConverter'),
]
