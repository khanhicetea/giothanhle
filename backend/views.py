from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Area, Church

def index(request):
    return JsonResponse({"IN GOD": "WE TRUST"})

def list_areas(request):
    areas = Area.objects.all()
    return JsonResponse({"data": [a.to_json() for a in areas]})

def list_churches(request):
    churches = Church.objects.all()
    return JsonResponse({"data": [c.to_json() for c in churches]})