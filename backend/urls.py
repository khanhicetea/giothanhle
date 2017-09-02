from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='backend_index'),
    url(r'^areas$', views.list_areas, name='backend_list_areas'),
    url(r'^churches$', views.list_churches, name='backend_list_churches'),
]
