from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import *
from .templates import *
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse


def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def pertsonak(request):
  mypertsona = Pertsona.objects.all()
  template = loader.get_template('pertsonak.html')
  context = {
    'mypertsona': mypertsona,
  }
  return HttpResponse(template.render(context, request))


def kotxeak(request):
  mykotxea = Kotxea.objects.all()
  template = loader.get_template('kotxeak.html')
  context = {
    'mykotxea': mykotxea,
  }
  return HttpResponse(template.render(context, request))


def delpertsona(request, id):
  Pertsona.objects.get(id=id).delete()
  return HttpResponseRedirect(reverse('pertsonak'))


def delkotxea(request, id):
  Kotxea.objects.get(id=id).delete()
  return HttpResponseRedirect(reverse('kotxeak'))

def addpertsona(request):
  template = loader.get_template('addpertsona.html')
  return HttpResponse(template.render())

def addkotxea(request):
  mypertsona = Pertsona.objects.all()
  template = loader.get_template('addkotxea.html')
  context = {
    'mypertsona': mypertsona,
  }
  return HttpResponse(template.render(context, request))


@csrf_exempt
def addpertsonatodb(request):
  name = request.POST['name']
  pertsona = Pertsona(name=name)
  pertsona.save()
  return HttpResponseRedirect(reverse('pertsonak'))


@csrf_exempt
def addkotxeatodb(request):
  modeloa = request.POST['modeloa']
  data = request.POST['data']
  pertsonaid = request.POST['pertsona']
  pertsonaobj = Pertsona.objects.get(id=pertsonaid)
  kotxea = Kotxea(modeloa=modeloa, data=data, pertsona=pertsonaobj)
  kotxea.save()
  return HttpResponseRedirect(reverse('kotxeak'))

def updatepertsona(request, id):
  pertsona = Pertsona.objects.get(id=id)
  template = loader.get_template('updatepertsona.html')
  context = {
    'pertsona': pertsona,
  }
  return HttpResponse(template.render(context, request))

def updatekotxea(request, id):
  kotxea = Kotxea.objects.get(id=id)
  mypertsona = Pertsona.objects.all()
  template = loader.get_template('updatekotxea.html')
  context = {
    'kotxea': kotxea,
    'mypertsona': mypertsona,
  }
  return HttpResponse(template.render(context, request))


@csrf_exempt
def updatepertsonaondb(request, id):
  pertsonaid = Pertsona.objects.get(id=id)
  name = request.POST['name']
  pertsona = Pertsona(id=pertsonaid.id, name=name)
  pertsona.save()
  return HttpResponseRedirect(reverse('pertsonak'))


@csrf_exempt
def updatekotxeaondb(request, id):
  kotxea = Kotxea.objects.get(id=id)
  modeloa = request.POST['modeloa']
  data = request.POST['data']
  pertsonaid = request.POST['pertsona']
  pertsonaobj = Pertsona.objects.get(id=pertsonaid)
  kotxea = Kotxea(id=kotxea.id, modeloa=modeloa, data=data, pertsona=pertsonaobj)
  kotxea.save()
  return HttpResponseRedirect(reverse('kotxeak'))



