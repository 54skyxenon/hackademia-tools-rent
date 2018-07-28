from django.contrib import admin
from django.urls import path
from django_backend.views import *

urlpatterns = [
    path('', HomeView),
]
