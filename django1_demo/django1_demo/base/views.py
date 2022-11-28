from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
  template = loader.get_template('hello.html')
  return HttpResponse(template.render())

def index1(request):
  template = loader.get_template('goodbye.html')
  return HttpResponse(template.render())

def index2(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
