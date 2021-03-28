from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('RenderTemplate', views.renderTemplate, name='renderTemplate'),
    path('path_converter/<int:num>', views.PathConverterExample, name='Path Converter'),
]
