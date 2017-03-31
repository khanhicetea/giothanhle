from django.shortcuts import render
from django.http import HttpResponse
from .models import Area, Church

def index(request):
    return HttpResponse("Hello world, IN GOD WE TRUST !!!")

def areas_js(request):
    areas = Area.objects.all()
    return render(request, 'templates/areas.js.j2', {
        'areas': areas
    },content_type='application/javascript')

def churches_js(request):
    churches = Church.objects.all()
    return render(request, 'templates/churches.js.j2', {
        'churches': churches
    },content_type='application/javascript')
