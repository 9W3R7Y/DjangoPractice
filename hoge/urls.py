from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('RenderTemplate', views.RenderTemplateExample, name='renderTemplate'),
    path('<int:num>', views.PathConverterExample, name='Path Converter'),
]
