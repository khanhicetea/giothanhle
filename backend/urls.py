from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='admin_dashboard'),
    url(r'^churches.js$', views.churches_js, name='backend_churches_js'),
    url(r'^areas.js$', views.areas_js, name='backend_areas_js'),    
]
