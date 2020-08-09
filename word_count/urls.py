from django.urls import path
from . import viewz

urlpatterns = [
        path('', viewz.hithere, name='home'),
        path('count/', viewz.Count, name='countwords'),
        path('about/', viewz.about, name='about')
        ]
