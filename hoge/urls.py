from django.urls import path

from . import views

app_name = "hoge"
urlpatterns = [
    path('', views.index, name='index'),
    path('render_template', views.RenderTemplateExample, name='render_template'),
    path('<int:num>', views.PathConverterExample, name='path_converter'),
    path('form', views.FormExample, name='from'),
    path('submit', views.SubmitExample, name='submit'),
    path('submitted/<str:form_value>', views.SubmittedExample, name='submitted'),
]
