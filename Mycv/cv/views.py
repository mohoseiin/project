from django.template import loader
from django.http import HttpResponse

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def cv(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def create(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def store(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def edit(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def update(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def delete(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())