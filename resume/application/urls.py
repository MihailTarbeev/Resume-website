from django.contrib import admin
from django.urls import path
from application.views import index

urlpatterns = [
    path('', index, name='home'),
    ]
