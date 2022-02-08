import imp
from unicodedata import name
from django.urls import path
from catalogo import views

urlpatterns = [
  path('', views.index, name='index')
]