from django.contrib import admin
from django.urls import path,include
from django.urls import re_path as url
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/survivor/', views.survivor_create),
    url(r'^api/v1/survivor/(?P<pk>[0-9]+)/$', views.survivor_update),
    url(r'^api/v1/survivor/survivors_infected/$', views.infected_survivors_report),
    url(r'^api/v1/survivor/survivors_no_infected/$', views.no_infected_survivor_report),
    
]