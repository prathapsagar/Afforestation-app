from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'mapp'
urlpatterns = [
    path('', TemplateView.as_view(template_name='mapp/index.html')),
    path('mapp/out', 
        views.MapCreateView.as_view(), name='map'),

]